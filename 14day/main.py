""" 
Day 14 of Advent of Code 2024
https://adventofcode.com/2024/day/14
"""
import os
import sys
import re


DEFAULT_FILE_NAME = "input.txt"
SECONDS = 100

def extract_numbers(text) -> list:
    """
    Extract all numeric sequences from the given text.

    Args:
        text (str): The input string from which to extract numbers.

    Returns:
        list: A list of strings, each representing a sequence of digits found in the text.
    """
    return re.findall(r'-?\d+', text)

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

def get_position_and_velocity(file_data: list) -> list:
    position_and_velocity = []
    for line in file_data:
        position_and_velocity.append([int(num) for num in extract_numbers(line)])
    return position_and_velocity

def move_robots(position_and_velocity, is_test):
    if is_test:
        rows =7
        cols = 11
        quad_1_3_x = range(0,5)
        quad_2_4_x = range(6,11)
        quad_1_4_y = range(0,3)
        quad_2_3_y = range(4,7)
    else:
        rows = 103
        cols = 101
        quad_1_3_x = range(0,50)
        quad_2_4_x = range(51,101)
        quad_1_4_y = range(0,51)
        quad_2_3_y = range(52,103)
        
    quad = [0,0,0,0]
    
    for robot in position_and_velocity:
        print(f"Start = {robot[0]}, {robot[1]} Vel = {robot[2]},{robot[3]}")
        robot[0] = (robot[0] + robot[2] * SECONDS) % cols
        robot[1] = (robot[1] + robot[3] * SECONDS) % rows
        if robot[0] in quad_1_3_x and robot[1] in quad_1_4_y:
            quad[0] += 1
        if robot[0] in quad_1_3_x and robot[1] in quad_2_3_y:
            quad[2] += 1
        if robot[0] in quad_2_4_x and robot[1] in quad_1_4_y:
            quad[3] += 1
        if robot[0] in quad_2_4_x and robot[1] in quad_2_3_y:
            quad[1] += 1
        print(robot[0], robot[1])
    print(quad)
    return quad[0] * quad[1] * quad[2] * quad[3]

        

def main():
    """ Main function
        Reads the specified input file
        Splits the data into a 2d map - comment line if data is not a map
        
    """
    file_name = get_file_name()
    is_test =  "test" in file_name
    file_data = read_input(file_name)
    position_and_velocity = get_position_and_velocity(file_data)
    result = move_robots(position_and_velocity,is_test)
    print(result)


if __name__ == "__main__":
    main()
