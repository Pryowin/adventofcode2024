""" 
Day 3 of Advent of Code 2024
https://adventofcode.com/2024/day/3
"""
import os
import re
import sys

DEFAULT_FILE_NAME = "input.txt"

def read_input(file_name:str) -> str:
    """Read input file

    Args:
        file_name (str): Name of the input file
        File is in same location as the python code
        
    Returns:
        A string with the contents of the file
    """
    file = os.path.join(os.path.dirname(__file__), file_name)
    with open(file, encoding="utf-8") as input_data:
        return input_data.read()
    

def get_file_name() -> str:
    """ Returns the base file name for the input to problem
    Return: If no args were provided when program was run, returns the default
    Otherwise it returns the file name provided on the command line
    """
    if len(sys.argv) == 1:
        return DEFAULT_FILE_NAME
    return sys.argv[1]

def find_valid_instructions(memory: str) -> list:
    return re.findall(r"mul\(\d{1,3},\d{1,3}\)",memory)

def process_instructions(instructions: list) -> int:
    count = 0
    for instruction in instructions:
        edited_instruction = re.sub(r"mul\(|\)","",instruction)
        numbers = edited_instruction.split(",")
        count += int(numbers[0]) * int(numbers[1])
    return count

def main():
    """ Main function
        Reads the specified input file
        
    """
    file_name = get_file_name()
    memory = read_input(file_name)
    valid_instructions = find_valid_instructions(memory)
    total = process_instructions(valid_instructions)
    print(total)
    

if __name__ == "__main__":
    main()
