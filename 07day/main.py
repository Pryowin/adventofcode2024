""" 
Day x of Advent of Code 2024
https://adventofcode.com/2024/day/x
"""
import os
import sys
from itertools import product

DEFAULT_FILE_NAME = "input.txt"

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

def count_valid_equations(file_data) -> int:
    sum_valid = 0
    for line in file_data:
        parts = line.strip().split(":")
        answer = int(parts[0])
        numbers = [int(n) for n in parts[1].split()]
        operator_combinations = list(product(["+", "*"], repeat = len(numbers)-1))
        not_yet_verified = True
        for operators in operator_combinations:
            result = numbers[0]
            for i, op in enumerate(operators):
                if op == "*":
                    result *= numbers[i+1]
                else:
                    result += numbers[i+1]
            if answer == result and not_yet_verified:
                not_yet_verified = False
                sum_valid += result
    return sum_valid

def main():
    """ Main function
        Reads the specified input file
        
    """
    file_name = get_file_name()
    file_data = read_input(file_name)
    print(count_valid_equations(file_data))

if __name__ == "__main__":
    main()
