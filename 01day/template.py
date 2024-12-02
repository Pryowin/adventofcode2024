""" 
Day x of Advent of Code 2024
https://adventofcode.com/2024/day/x
"""
import os
import sys

def read_input(file_name:str):
    """Read input file

    Args:
        file_name (str): Name of the input file
        File is in same location as the python code
    """
    file = os.path.join(os.path.dirname(__file__), file_name)
    with open(file, encoding="utf-8") as input_data:
        pass

def main():
    """ Main function
        Reads the specified input file
        
    """
    if len(sys.argv) == 1:
        file_name = "input.txt"
    else:
        file_name = sys.argv[1]

    read_input(file_name)

if __name__ == "__main__":
    main()
