""" 
Day 10 of Advent of Code 2024
https://adventofcode.com/2024/day/10
"""
import os
import sys

DEFAULT_FILE_NAME = "input.txt"
DIRECTIONS = [(-1,0),(1,0),(0,1),(0,-1)]

class Counts:
    """
    A class to manage and track counts for two separate parts.

    Attributes:
        _part_1 (int): Counter for part 1.
        _part_2 (int): Counter for part 2.

    Methods:
        inc_part_1(): Increments the counter for part 1 by 1.
        inc_part_2(): Increments the counter for part 2 by 1.
        part_1() -> int: Returns the current count for part 1.
        part_2() -> int: Returns the current count for part 2.
    """
    def __init__(self):
        self._part_1 = 0
        self._part_2 = 0
    
    def inc_part_1 (self):
        """Increments the counter for part 1 by 1"""
        self._part_1 += 1
    
    def inc_part_2 (self):
        """Increments the counter for part 2 by 1"""
        self._part_2 += 1
    
    def part_1(self) ->int:
        """ Returns the current count for part 1"""
        return self._part_1
    
    def part_2(self) ->int:
        """ Returns the current count for part 2"""
        return self._part_2
        

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

def get_trail_heads(topographic_map:list) -> list:
    """
    Identifies and returns the coordinates of trail heads in a topographic map.

    A trail head is defined as a point with a height of "0" in the map.

    Args:
        topographic_map (list): A 2D list representing the topographic map, where each element is a character indicating the height.

    Returns:
        list: A list of tuples, each containing the (y, x) coordinates of a trail head.
    """
    trail_heads = list()
    for y,_ in enumerate(topographic_map):
        for x,height in enumerate(topographic_map[y]):
            if height == "0":
                trail_heads.append((y,x))
    return trail_heads

def count_paths(topographic_map: list, trail_heads: list,counts: Counts):
    """
    Counts the number of valid paths from each trail head in the topographic map.

    This function iterates over a list of trail heads and calls the
    `count_paths_from_head` function for each, tracking visited paths
    to avoid counting duplicates.

    Args:
        topographic_map (list): A 2D list representing the topographic map.
        trail_heads (list): A list of tuples representing the starting points
                            for path counting.
    """
    visited = set()
    for trail_head in trail_heads:
        count_paths_from_head(topographic_map,trail_head,trail_head,visited,counts)


def count_paths_from_head(topographic_map: list, 
                          location: tuple,
                          start: tuple,
                          visited: set,
                          counts: Counts) -> None:
    """
    Recursively counts paths in a topographic map starting from a given location.

    This function explores all possible paths from the current location in the
    topographic map, incrementing counts based on specific conditions. It checks
    adjacent cells to see if they form a valid path by increasing in value by 1.
    If a path reaches a value of 9, it updates the counts accordingly.

    Parameters:
        topographic_map (list): A 2D list representing the topographic map.
        location (tuple): The current location in the map as (row, column).
        start (tuple): The starting location of the path.
        visited (set): A set of visited paths to avoid revisiting.
        counts (Counts): An instance of the Counts class to track path counts.

    Returns:
        None
"""
    start_value = int(topographic_map[location[0]][location[1]])
    rows = len(topographic_map)
    cols = len(topographic_map[0])
    for direction in DIRECTIONS:
        new_loc = (location[0] + direction[0], location[1] + direction[1])
        if 0 <= new_loc[0] < rows and 0 <= new_loc[1] < cols:
            new_value = int(topographic_map[new_loc[0]][new_loc[1]])
            if new_value == start_value +1:
                if new_value == 9:
                    if not (start,new_loc) in visited:
                        counts.inc_part_1()
                        visited.add((start, new_loc))
                    counts.inc_part_2()
                else:
                    count_paths_from_head(topographic_map, new_loc, start, visited,counts)


def main():
    """ Main function
        Reads the specified input file
        Creates a 2-D array of characters
        Initializes an instance of Counts
        Counts paths for both Part 1 and Part 2
        Prints the results
    """
    file_name = get_file_name()
    file_data = read_input(file_name)
    topographic_map = [list(s.strip()) for s in file_data]
    trail_heads = get_trail_heads(topographic_map)
    counts = Counts()
    count_paths(topographic_map,trail_heads,counts)
    print(counts.part_1())
    print(counts.part_2())

if __name__ == "__main__":
    main()
