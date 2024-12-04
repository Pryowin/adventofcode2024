""" 
Day 4 of Advent of Code 2024
https://adventofcode.com/2024/day/4
"""
import os
import sys
from itertools import product

DEFAULT_FILE_NAME = "input.txt"
WORD = 'XMAS'
WORD_LEN = len(WORD)
FIRST_LETTER = "X"
FIRST_CROSS = "M"
LAST_CROSS = "S"
CENTER_CROSS = "A"

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
            file_data.append(line.strip())
    return file_data

def get_file_name() -> str:
    """ Returns the base file name for the input to problem
    Return: If no args were provided when program was run, returns the default
    Otherwise it returns the file name provided on the command line
    """
    if len(sys.argv) == 1:
        return DEFAULT_FILE_NAME
    return sys.argv[1]

def create_matrix(file_data) -> list:
    """
    Converts a list of strings into a matrix (list of lists), where each string
    is split into a list of its characters.

    Args:
        file_data (list of str): A list of strings to be converted into a matrix.

    Returns:
        list: A matrix representation of the input data, with each string
        converted into a list of characters.
    """
    matrix =[None] * len(file_data) 
    index = -1
    for line in file_data:
        index += 1
        matrix[index] = list(line)
    return matrix

def process_puzzle(puzzle:list ,row_count:int ,column_count:int ) -> int:
    """
    Processes a puzzle grid to count the number of words found.

    Iterates over each cell in the puzzle grid, checking for the presence
    of the character 'X'. For each 'X' found, it calls the `words_found`
    function to determine the number of occurrences of XMAS that can be formed starting
    from that position in various directions.

    Args:
        puzzle (list of list of str): The puzzle grid represented as a 2D list.
        row_count (int): The number of rows in the puzzle grid.
        column_count (int): The number of columns in the puzzle grid.

    Returns:
        int: The total count of words found in the puzzle grid.
    """
    count = 0
    for y in range(0,row_count):
        for x in range(0,column_count):
            if puzzle[y][x] == FIRST_LETTER:
                count += words_found(puzzle, y,x, row_count, column_count)
    return count

def words_found(puzzle:list , y:int,x:int, row_count:int ,column_count:int ) -> int:
    """
    Counts the occurrences of the predefined word in all possible directions
    from a given starting position in a 2D puzzle grid.

    Args:
        puzzle (list of list of str): The 2D grid representing the puzzle.
        y (int): The starting row index in the puzzle.
        x (int): The starting column index in the puzzle.
        row_count (int): The total number of rows in the puzzle.
        column_count (int): The total number of columns in the puzzle.

    Returns:
        int: The number of times the word is found starting from the given position.
    """
    count = 0
    directions = list(product([-1,0,1],[-1,0,1] ))
    directions.remove((0,0))
    for vertical_direction, horizontal_direction in directions:
        if 0 <= y + vertical_direction * (WORD_LEN-1) < row_count:
            if 0 <= x + horizontal_direction * (WORD_LEN-1) < column_count:
                if is_word_found(puzzle,y,x,vertical_direction,horizontal_direction):
                    count += 1
    return count
                        
def is_word_found(puzzle:list , start_y:int ,start_x:int,
                  vertical_direction:int,horizontal_direction:int) -> bool:
    """
    Checks if the predefined word 'XMAS' can be found in the given puzzle starting
    from a specified position and moving in a specified direction.

    Args:
        puzzle (list of list of str): The 2D grid of characters to search within.
        start_y (int): The starting row index in the puzzle.
        start_x (int): The starting column index in the puzzle.
        vertical_direction (int): The vertical movement direction (1 for down, -1 for up).
        horizontal_direction (int): The horizontal movement direction (1 for right, -1 for left).

    Returns:
        bool: True if the word 'XMAS' is found in the specified direction, False otherwise.
    """
    word_len = len(WORD)
    char_list = []
    y = start_y
    x = start_x
    for _ in range (0,word_len):
        char_list.append(puzzle[y][x])
        y += vertical_direction
        x += horizontal_direction
    return ''.join(char_list) == WORD
          
def process_puzzle_part_2(puzzle:list , row_count:int, column_count:int) -> int:
    """
    Processes the puzzle to count occurrences of a specific pattern.

    Iterates over the puzzle grid, checking for cells marked 'A' and
    determines if a cross pattern is found using the `cross_found` function.
    Counts and returns the number of such patterns found.

    Args:
        puzzle (list of list of str): The puzzle grid to be processed.
        row_count (int): The number of rows in the puzzle.
        column_count (int): The number of columns in the puzzle.

    Returns:
        int: The count of cross patterns found in the puzzle.
    """
    count = 0
    for y in range(1,row_count-1):
        for x in range(1,column_count-1):
            if puzzle[y][x] == CENTER_CROSS:
                if cross_found(puzzle,y,x):                
                    count += 1
    return count

def cross_found(puzzle,y,x) -> bool:
    """
    Checks if a specific cross pattern is found in the puzzle at the given coordinates.

    The function examines the surrounding elements of the specified position (y, x) 
    in the puzzle to determine if there are two specific cross patterns formed by 
    the characters 'M' and 'S'. Returns True if both patterns are found, otherwise 
    returns False.

    Args:
        puzzle (list of list of str): A 2D list representing the puzzle grid.
        y (int): The y-coordinate (row index) in the puzzle.
        x (int): The x-coordinate (column index) in the puzzle.

    Returns:
        bool: True if the cross pattern is found, False otherwise.
    """
    count = 0
    if puzzle[y-1][x-1] == FIRST_CROSS and puzzle[y+1][x+1] == LAST_CROSS:
        count += 1
    if puzzle[y-1][x-1] == LAST_CROSS and puzzle[y+1][x+1] == FIRST_CROSS:
        count += 1
    if puzzle[y-1][x+1] == FIRST_CROSS and puzzle[y+1][x-1] == LAST_CROSS:
        count += 1
    if puzzle[y-1][x+1] == LAST_CROSS and puzzle[y+1][x-1] == FIRST_CROSS:
        count += 1
    return count == 2
    
def main():
    """ Main function
        Reads the specified input file
        Runs Part 1 and Part 2 of the puzzle 
        Prints the result for each part
    """
    file_name = get_file_name()
    file_data = read_input(file_name)
    ## PART 1
    puzzle = create_matrix(file_data)
    count = process_puzzle(puzzle, len(file_data), len(puzzle[0]))
    print(count)
    
    ## PART 2
    count = process_puzzle_part_2(puzzle, len(file_data), len(puzzle[0]))
    print(count)

if __name__ == "__main__":
    main()
