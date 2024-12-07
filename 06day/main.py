""" 
Day 6 of Advent of Code 2024
https://adventofcode.com/2024/day/6
"""
import os
import sys

from copy import deepcopy

DEFAULT_FILE_NAME = "input.txt"
GUARD_DIRECTION = {"v": (1,0), "^": (-1,0), ">" : (0,1), "<": (0,-1)}
GUARD_TURN = {"v": "<", "<": "^", "^": ">", ">":"v" }
OBSTACLE = "#"

rows=0 
cols=0

X_IDX = 1
Y_IDX = 0

class Guard():
    def __init__(self, y,x, icon) -> None:
        self._y = y
        self._x = x
        self._icon = icon
        self._direction = GUARD_DIRECTION[icon]
        
    def x(self):
        return self._x
    def y(self):
        return self._y
    def new_x(self):
        return self._x + self._direction[X_IDX]
    def new_y(self):
        return self._y + self._direction[Y_IDX]
    def icon(self):
        return self._icon
        
    def is_move_in_bounds(self) ->bool:
        new_x = self._x + self._direction[X_IDX]
        new_y = self._y + self._direction[Y_IDX]
        return self._is_in_bounds(new_y,new_x)
    
    def _is_in_bounds(self,y,x) -> bool:
        return (0 <= y < rows)  and (0 <= x < cols)
    
    def is_in_bounds(self) -> bool:
        return self._is_in_bounds(self._y,self._x)
        
    def move(self):
        self._x = self._x + self._direction[X_IDX]
        self._y = self._y + self._direction[Y_IDX]
        
    def rotate(self):
        self._icon = GUARD_TURN[self._icon]
        self._direction = GUARD_DIRECTION[self._icon]
        
    def obstacle(self,grid) -> bool:
        new_x = self._x + self._direction[X_IDX]
        new_y = self._y + self._direction[Y_IDX]
        return grid[new_y][new_x] == OBSTACLE
    
    def vector_pos(self) -> tuple:
        return (self._y, self._x,self._icon)
    
    def pos(self) -> tuple:
        return (self._y, self._x)

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

def find_position_and_direction(grid) -> Guard:
    icon = ''
    for y in range(rows):
        for x in range(cols):
            contents = grid[y][x]
            if contents not in (".","#"):   
                pos_x = x
                pos_y = y
                icon = contents
                break
    return Guard(pos_y,pos_x,icon)

def move_and_count(grid: list,guard: Guard) -> int:
    positions = set()

    while guard.is_in_bounds():
        has_updated = False
        positions.add(guard.pos())
        if guard.is_move_in_bounds():
            if guard.obstacle(grid):
                guard.rotate()
                has_updated = True
        if not has_updated:
            guard.move()
            
    return len(positions)

def move_and_count_blocks(grid: list ,guard: Guard) ->int:
    block_positions = set()
    while guard.is_in_bounds():
        if guard.is_move_in_bounds():
            if not guard.obstacle(grid):
                new_y = guard.new_y()
                new_x = guard.new_x()
                if not (guard.pos() in block_positions):
                    grid[new_y][new_x] = OBSTACLE
                    if is_loop(grid, deepcopy(guard)):
                        block_positions.add(guard.pos())
                    grid[new_y][new_x] = '.'
                guard.move()
            else:
                guard.rotate()
        else:
            guard.move()
    
    return len(block_positions)
            

def is_loop(grid:list, guard:Guard) -> bool:
    positions = set()
    while guard.is_in_bounds():
        positions.add(guard.vector_pos())
        if guard.is_move_in_bounds():
            if guard.obstacle(grid):
                guard.rotate()
            else:
                guard.move()
        else:
            return False
        if guard.vector_pos() in positions:
            return True
            
    
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
    guard = find_position_and_direction(grid)
    unique_locations = move_and_count(grid,guard)
    print(unique_locations)
    
    guard = find_position_and_direction(grid)
    block_locations = move_and_count_blocks(grid,guard)
    print(block_locations)
    

if __name__ == "__main__":
    main()
