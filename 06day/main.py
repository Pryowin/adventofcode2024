""" 
Day 6 of Advent of Code 2024
https://adventofcode.com/2024/day/6
"""
import os
import sys

DEFAULT_FILE_NAME = "input.txt"
GUARD_DIRECTION = {"v": (1,0), "^": (-1,0), ">" : (0,1), "<": (0,-1)}
GUARD_TURN = {"v": "<", "<": "^", "^": ">", ">":"v" }
Y_IDX = 0
X_IDX = 1
POS_IDX = 0
DIR_IDX = 1
ICON_IDX = 2

rows=0 
cols=0

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

def find_position_and_direction(grid) -> tuple:
    icon = ''
    for y in range(rows):
        for x in range(cols):
            contents = grid[y][x]
            if contents not in (".","#"):   
                pos_x = x
                pos_y = y
                direction = GUARD_DIRECTION[contents]
                icon = contents
                break
    return ((pos_y,pos_x),direction,icon)

def move_and_count(grid: list) -> int:
    positions = set()
    guard = find_position_and_direction(grid)
    while is_guard_in_bounds(guard):
        positions.add(guard[POS_IDX])
        guard = move_guard(grid, guard)
    return len(positions)

def is_guard_in_bounds(guard):
    y = guard[POS_IDX][Y_IDX]
    x = guard[POS_IDX][X_IDX]
    return (0 <= y < rows) and (0 <= x < cols)

def move_guard(grid, guard) -> tuple:
    y = guard[POS_IDX][Y_IDX]
    x = guard[POS_IDX][X_IDX]
    direction = guard[DIR_IDX]
    icon = guard[ICON_IDX]
    new_x = x + direction[X_IDX]
    new_y =y + direction[Y_IDX]
    new_guard = ((new_y,new_x),direction,icon)
    if is_guard_in_bounds(new_guard):
        if grid[new_y][new_x] == "#":
            new_icon = GUARD_TURN[icon]
            new_direction = GUARD_DIRECTION[new_icon]
            return((y,x),new_direction,new_icon)
    return ((new_y,new_x),direction,icon)

def main():
    """ Main function
        Reads the specified input file
        
    """
    file_name = get_file_name()
    file_data = read_input(file_name)
    grid = [None] * len(file_data)
    for i,line in enumerate(file_data):
        grid[i] = list(line.strip() )
    global rows
    global cols
    rows = len(grid)
    cols = len(grid[0])
    unique_locations = move_and_count(grid)
    print(unique_locations)
    

if __name__ == "__main__":
    main()
