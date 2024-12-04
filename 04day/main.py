""" 
Day 4 of Advent of Code 2024
https://adventofcode.com/2024/day/4
"""
import os
import sys

DEFAULT_FILE_NAME = "input.txt"
WORD = 'XMAS'

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
    matrix =[None] * len(file_data) 
    index = -1
    for line in file_data:
        index += 1
        matrix[index] = list(line)
    return matrix    
    
def process_puzzle(puzzle,row_count,column_count) -> int:
    count = 0
    for y in range(0,row_count):
        for x in range(0,column_count):
            if puzzle[y][x] == 'X':
                count += words_found(puzzle, y,x, row_count, column_count)
        
    return count

def words_found(puzzle, y,x, row_count,column_count) -> int:
    count = 0
    word_len = len(WORD)
    for vertical_direction in [-1,0,1]:
        for horizontal_direction in [-1,0,1]:
            if not (vertical_direction == 0 and horizontal_direction == 0):
                if 0 <= y + vertical_direction * (word_len-1) < row_count:
                    if 0 <= x + horizontal_direction * (word_len-1) < column_count:
                        if is_word_found(puzzle,y,x,vertical_direction,horizontal_direction):
                            count += 1
    return count
                        
def is_word_found(puzzle, start_y,start_x,vertical_direction,horizontal_direction) -> bool:
    word_len = len(WORD)
    found_word = ""
    y = start_y
    x = start_x
    for _ in range (0,word_len):
        found_word += puzzle[y][x]
        y += vertical_direction
        x += horizontal_direction
    return found_word == WORD
          
    
def main():
    """ Main function
        Reads the specified input file
        
    """
    file_name = get_file_name()
    file_data = read_input(file_name)
    puzzle = create_matrix(file_data)
    count = process_puzzle(puzzle, len(file_data), len(puzzle[0]))
    print(count)

if __name__ == "__main__":
    main()
