""" 
Day x of Advent of Code 2024
https://adventofcode.com/2024/day/x
"""
import os
import sys
from itertools import product
from time import time

DEFAULT_FILE_NAME = "input.txt"
MULTIPLY = "*"
ADD = "+"
CONCAT = "||"

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

def count_valid_equations(file_data, is_part_one = True) -> int:

    """
    Counts the number of valid equations from the provided file data.

    Each line in the file data contains an expected answer and a sequence of numbers.
    The function evaluates all possible equations using the numbers and a set of operators
    to determine if they match the expected answer. The operators used depend on the
    is_part_one flag.

    Args:
        file_data (list of str): List of strings, each representing a line with an expected
                                answer and a sequence of numbers.
        is_part_one (bool): Flag to determine the set of operators to use. If True, only
                            "+" and "*" are used. If False, "||" is also included.

    Returns:
        int: The sum of all valid equations that match the expected answers.
    """
    sum_valid = 0
    start = time()
    for line in file_data:
        parts = line.strip().split(":")
        answer = int(parts[0])
        numbers = [int(n) for n in parts[1].split()]
        num_operators = len(numbers) -1
        if is_part_one:
            operator_combinations = list(product([ADD, MULTIPLY], repeat=num_operators))
        else:
            operator_combinations = list(product([ADD, MULTIPLY, CONCAT], repeat=num_operators))
        not_yet_verified = True
        for operators in operator_combinations:
            result = numbers[0]
            for i, op in enumerate(operators):
                match op:
                    case "*": # Multiply
                        result *= numbers[i+1]
                    case "+": # Add
                        result += numbers[i+1]
                    case "||": # Concatenate
                        result = int(str(result) + str(numbers[i+1]))
                    case _:
                        raise ValueError("Invalid operator")
                if result > answer:
                    break
            if answer == result and not_yet_verified:
                not_yet_verified = False
                sum_valid += result
    print (f"Time taken = {time()-start}")
    return sum_valid

def main():
    """ Main function
        Reads the specified input file
        
    """
    file_name = get_file_name()
    file_data = read_input(file_name)
    print(count_valid_equations(file_data))
    print(count_valid_equations(file_data,False))

if __name__ == "__main__":
    main()
