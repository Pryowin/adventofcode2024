""" 
Day x of Advent of Code 2024
https://adventofcode.com/2024/day/x
"""
import os
import sys
from copy import deepcopy

DEFAULT_FILE_NAME = "input.txt"
FREE_SPACE = '.'

def read_input(file_name:str) -> str:
    """Read input file

    Args:
        file_name (str): Name of the input file
        File is in same location as the python code
        
    Returns:
        A list of the lines in the file
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

def create_map(input_data: list) ->tuple[list,dict,dict,int]:
    disk_map=[]
    free_space_blocks = dict()
    file_blocks = dict()
    for i,value in enumerate(input_data):
        if (i%2) == 0:
            file_num = int((i/2))
            char = str(file_num)
            file_blocks[char] = value
        else:
            char = FREE_SPACE
            pos = '{0:07d}'.format(len(disk_map))
            free_space_blocks[pos] = int(value)
        for _ in range(int(value)):
            disk_map.append(char)
    return disk_map,free_space_blocks,file_blocks,file_num
        

def last_index(lst: list) ->int:
    idx = len(lst)
    while lst[idx-1] == FREE_SPACE:
        idx -= 1
    return idx
        
def compact(disk_map: list) -> list:
    last_free_space = last_index(disk_map)
    while last_free_space != disk_map.index(FREE_SPACE):
        first_free_space = disk_map.index(FREE_SPACE)
        x = disk_map[last_free_space - 1]
        y = disk_map[first_free_space]
        disk_map[last_free_space - 1] = y
        disk_map[first_free_space] = x
        last_free_space -= 1
    return disk_map

def checksum(disk_map: list) -> int:
    check_sum_value = 0
    for i,value in enumerate(disk_map):
        if value != FREE_SPACE:
            check_sum_value += i * int(value)
    return check_sum_value

def compact_without_fragmentation(disk_map,free_space_map,file_map,file_count) -> list:
    while file_count > 0:
        file_size = int(file_map[str(file_count)])
        for key in sorted(free_space_map.keys()):
            free_space = int(free_space_map[key])
            if free_space >= file_size:
                del free_space_map[key]
                new_free = int(key) + file_size
                free_space_map[ '{0:07d}'.format(new_free)] = free_space - file_size
                new_start = int(key)
                old_start = disk_map.index(str(file_count))
                file = disk_map[old_start : old_start +  file_size]
                disk_map[old_start : old_start + file_size] = disk_map[new_start : new_start + file_size]
                disk_map[new_start : new_start + file_size] = file
                break
        file_count -= 1
    return disk_map
    
def main():
    """ Main function
        Reads the specified input file
        
    """
    file_name = get_file_name()
    file_data = read_input(file_name)
    disk_map, free_space_map, file_map,file_count = create_map(list(file_data.strip()))
    compacted_map = compact(deepcopy(disk_map))
    print(checksum(compacted_map))
  
    compacted_map_no_frag = compact_without_fragmentation(disk_map,free_space_map,file_map,file_count)
    print(checksum(compacted_map_no_frag))

if __name__ == "__main__":
    main()
