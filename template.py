""" 
Day x of Advent of Code 2024
https://adventofcode.com/2024/day/x
"""
import os
import sys
from itertools import product

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


def main():
    """ Main function
        Reads the specified input file
        Splits the data into a 2d map - comment line if data is not a map
        
    """
    file_name = get_file_name()
    file_data = read_input(file_name)
    data_2d = [list(s.strip()) for s in file_data]

if __name__ == "__main__":
    main()
