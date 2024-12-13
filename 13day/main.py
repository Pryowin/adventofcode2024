""" 
Day x of Advent of Code 2024
https://adventofcode.com/2024/day/x
"""
import os
import sys
import re
from itertools import product

import numpy as np


def get_directions(are_diagonals_valid = False) -> list:
    """
    Determines the set of directions based on the validity of diagonal movement.

    Returns:
        list: A list of tuples representing possible movement directions. If
        diagonal movement is valid, includes all combinations of (-1, 0, 1)
        except (0, 0). Otherwise, includes only cardinal directions.
    """
    if are_diagonals_valid:
        directions = list(product([-1, 0, 1], repeat=2))
        directions.remove(0,0)
    else:
        directions = [(-1,0),(1,0),(0,1),(0,-1)]
    return directions

DIRECTIONS = get_directions(False)
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
    return re.findall(r'\d+', text)

def solve(ax,ay, bx,by,px,py,is_part_one = True):
    left = np.array([[ax,ay],[bx,by]])
    right = np.array([px,py])
    solution = np.linalg.solve(left,right)
    is_valid = round(solution[0],3).is_integer() and round(solution[1],3).is_integer()
    
    return(is_valid, solution)
    
def process_input(file_data):
    i = 0
    line_count = len(file_data)
    answer = 0
    while i < line_count:
        text = f"{file_data[i]}{file_data[i+1]}{file_data[i+2]}"
        i += 4
        numbers = [int(num) for num in extract_numbers(text)]
        moves = solve(numbers[0],numbers[2],numbers[1],numbers[3],numbers[4],numbers[5])
        if moves[SOLUTION_EXISTS_IDX]:
            answer +=  moves[1][0] * COST_A + moves[1][1] * COST_B
    
    return answer
        
    
def main():
    """ Main function
        Reads the specified input file
        Splits the data into a 2d map - comment line if data is not a map
        
    """
    file_name = get_file_name()
    file_data = read_input(file_name)
    # data_2d = [list(s.strip()) for s in file_data]
    print(process_input(file_data))

if __name__ == "__main__":
    main()
