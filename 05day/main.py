""" 
Day 5 of Advent of Code 2024
https://adventofcode.com/2024/day/5
"""
import math
import os
import sys

DEFAULT_FILE_NAME = "input.txt"
RULE_SEP = '|'
UPDATE_SEP = ','

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

def get_rules(file_data) -> dict:
    rules = dict()
    for line in file_data:
        if line.strip() =='':
            break
        pages = line.strip().split(RULE_SEP)
        if pages[1] in rules:
            rules[pages[1]].append(pages[0])
        else:
            rules[pages[1]] = [pages[0]]     
    return rules

def get_updates(file_data) -> list:
    updates = []
    rules_ended = False
    for line in file_data:
        if rules_ended:
            updates.append(line.strip().split(UPDATE_SEP))
        if line.strip() == '':
            rules_ended = True
    return updates

def get_middle_index(array: list) -> int:
    return math.floor(len(array)/2)

        
def get_sum_of_valid_updates(page_updates, page_ordering_rules) -> int:
    count = 0
    for update in page_updates:
        middle = get_middle_index(update)
        valid = True
        for i,page in enumerate(update):
            if page in page_ordering_rules:
                for required_page in page_ordering_rules[page]:
                    if required_page in update:
                        idx = update.index(required_page)
                        if idx > i:
                            valid = False
        if valid:
            count += int(update[middle])
    return count
    

def main():
    """ Main function
        Reads the specified input file
        
    """
    file_name = get_file_name()
    file_data = read_input(file_name)
    page_ordering_rules = get_rules(file_data)
    page_updates  = get_updates(file_data)
    print(f"Part 1 for {file_name} = {get_sum_of_valid_updates(page_updates,page_ordering_rules)}")

if __name__ == "__main__":
    main()
