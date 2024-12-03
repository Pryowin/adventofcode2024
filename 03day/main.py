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

def remove_disabled_code(memory:str) -> str:   
    """
    Removes disabled code segments from the given memory string.

    This function processes the input string by splitting it into blocks
    using the delimiter "do()". Each block is further split by "don't()",
    and only the code before "don't()" is retained. The resulting enabled
    code segments are concatenated and returned as a single string.

    Parameters:
        memory (str): The input string containing code with "do()" and
                    "don't()" delimiters.

    Returns:
        str: A string containing only the enabled code segments.
    """    
    blocks = memory.split("do()")
    enabled_code = ''
    for block in blocks:
        sub_blocks = block.split("don't()")
        enabled_code += sub_blocks[0]
    return enabled_code

def find_valid_instructions(memory: str) -> list:
    """
    Find all valid 'mul' instructions in the given memory string.

    The function searches for non-overlapping occurrences of the pattern
    'mul(x,y)' where x and y are integers with 1 to 3 digits. Returns a
    list of all matches found.

    Args:
        memory (str): The string representing the memory to search within.

    Returns:
        list: A list of tuples, each containing a pair of numbers. 
    """
    matches = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)",memory)
    return  [(int(x), int(y)) for x, y in matches]

def process_instructions(pairs: list) -> int:
    """
    Processes a list of number pairs by multiplying each pair and summing the results.

    Args:
        pairs (list): A list of tuples, where each contains two numeric strings.

    Returns:
        int: The sum of the products of each pair of numbers.
    """
    count = 0
    for numbers in pairs:
        count += int(numbers[0]) * int(numbers[1])
    return count

def main():
    """ Main function
        Reads the specified input file
        Sums the valid instructions for Part 1
        Sums the valid instructions for Part 2
    """
    file_name = get_file_name()
    memory = read_input(file_name)
    valid_instructions = find_valid_instructions(memory)
    total = process_instructions(valid_instructions)
    print(total)
    # Part 2
    executable_code = remove_disabled_code(memory)
    valid_instructions = find_valid_instructions(executable_code)   
    total_2 = process_instructions(valid_instructions)
    print(total_2)


if __name__ == "__main__":
    main()
