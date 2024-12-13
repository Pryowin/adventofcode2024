""" 
Day 13 of Advent of Code 2024
https://adventofcode.com/2024/day/13
"""
import os
import sys
import re

import numpy as np

DEFAULT_FILE_NAME = "input.txt"
COST_A = 3
COST_B = 1
SOLUTION_EXISTS_IDX = 0
def read_input(file_name:str) -> list:
    """Read input file

    Args:
        file_name (str): Name of the input file
        File is in same location as the python code
        
    Returns:
        A list of the lines in the file
    """
    file_data = []
    file = os.path.join(os.path.dirname(__file__), file_name)
    with open(file, encoding="utf-8") as input_data:
        for line in input_data:
            file_data.append(line)
    return file_data

def get_file_name() -> str:
    """ Returns the base file name for the input to problem
    Return: If no args were provided when program was run, returns the default
    Otherwise it returns the file name provided on the command line
    """
    if len(sys.argv) == 1:
        return DEFAULT_FILE_NAME
    return sys.argv[1]

def extract_numbers(text) -> list:
    """
    Extract all numeric sequences from the given text.

    Args:
        text (str): The input string from which to extract numbers.

    Returns:
        list: A list of strings, each representing a sequence of digits found in the text.
    """
    return re.findall(r'\d+', text)

def solve(ax,ay, bx,by,px,py,is_part_one):
    """
    Solves a system of linear equations defined by two points and a target point.

    Parameters:
        ax (float): x-coordinate of the first point.
        ay (float): y-coordinate of the first point.
        bx (float): x-coordinate of the second point.
        by (float): y-coordinate of the second point.
        px (float): x-coordinate of the target point.
        py (float): y-coordinate of the target point.
        is_part_one (bool): Flag indicating whether to adjust the target point.

    Returns:
        tuple: A tuple containing a boolean indicating if the solution is valid 
        (both components are integers when rounded to three decimal places) and 
        the solution array of the linear equations.
    """
    left = np.array([[ax,ay],[bx,by]])
    if not is_part_one:
        px += 10000000000000
        py += 10000000000000
    right = np.array([px,py])
    solution = np.linalg.solve(left,right)
    is_valid = round(solution[0],3).is_integer() and round(solution[1],3).is_integer()
    return(is_valid, solution)

def process_input(file_data,is_part_one=True):
    """
    Processes the input data to calculate a total answer based on extracted numbers
    and their solutions from a system of linear equations.

    Parameters:
        file_data (list): A list of strings representing the input data.
        is_part_one (bool, optional): A flag indicating whether to adjust the target 
        point in the linear equations. Defaults to True.

    Returns:
        int: The calculated total answer based on the solutions of the linear equations.
    """
    i = 0
    line_count = len(file_data)
    answer = 0
    while i < line_count:
        text = f"{file_data[i]}{file_data[i+1]}{file_data[i+2]}"
        i += 4
        numbers = [int(num) for num in extract_numbers(text)]
        moves = solve(numbers[0],numbers[2],numbers[1],numbers[3],numbers[4],numbers[5],is_part_one)
        if moves[SOLUTION_EXISTS_IDX]:
            answer +=  moves[1][0] * COST_A + moves[1][1] * COST_B
    return answer

def main():
    """ Main function
        Reads the specified input file
        process the data for part 1 and part 2
    """
    file_name = get_file_name()
    file_data = read_input(file_name)
    # data_2d = [list(s.strip()) for s in file_data]
    print(process_input(file_data))
    print(process_input(file_data,False))

if __name__ == "__main__":
    main()
