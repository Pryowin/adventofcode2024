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
    """
    Parses the given file data to extract rules and returns them as a dictionary.

    Each line in the file data is expected to contain two page identifiers
    separated by a defined separator. The function maps the second page
    identifier to a list of first page identifiers.

    Args:
        file_data (iterable): An iterable containing lines of text representing rules.

    Returns:
        dict: A dictionary where keys are the second page identifiers and values
        are lists of first page identifiers.
    """
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
    """
    Extracts and returns a list of updates from the provided file data.

    The function processes lines from the input `file_data`, identifying the
    end of a rules section by an empty line. After this point, it collects
    subsequent lines as updates, splitting each line by the `UPDATE_SEP`
    delimiter.

    Args:
        file_data (iterable): An iterable containing lines of text data.

    Returns:
        list: A list of updates, where each update is a list of strings
        split by the `UPDATE_SEP` delimiter.
    """
    updates = []
    rules_ended = False
    for line in file_data:
        if rules_ended:
            updates.append(line.strip().split(UPDATE_SEP))
        if line.strip() == '':
            rules_ended = True
    return updates

def get_middle_index(array: list) -> int:
    """
    Calculate the middle index of a list.

    Args:
        array (list): The list for which to find the middle index.

    Returns:
        int: The middle index of the list, rounded down.
    """
    return math.floor(len(array)/2)

        
def get_sum_of_valid_updates(page_updates, page_ordering_rules) -> tuple:
    """
    Calculate the sum of valid page updates based on ordering rules.

    Iterates through a list of page updates, checking each update for validity
    according to specified page ordering rules. If an update is valid, its middle
    value is added to the first sum. If not, the sum of the fixed update is added
    to the second sum.

    Args:
        page_updates (list): A list of page updates, where each update is a list
            of pages.
        page_ordering_rules (dict): A dictionary defining the ordering rules for
            pages, where keys are pages and values are lists of required preceding
            pages.

    Returns:
        tuple: A tuple containing two integers. The first integer is the sum of
        the middle values of valid updates, and the second integer is the sum of
        the fixed updates.
    """
    count_part_1, count_part_2 = 0,0
    for update in page_updates:
        middle = get_middle_index(update)
        valid = True
        for i,page in enumerate(update):
            if  is_page_in_wrong_position(page,i, update, page_ordering_rules):
                valid = False
        if valid:
            count_part_1 += int(update[middle])
        else:
            count_part_2 += reorder_and_get_middle(update, page_ordering_rules)
            
    return (count_part_1,count_part_2)

def is_page_in_wrong_position(page, pos_of_page, update, page_ordering_rules) -> bool:
    """
    Determine if a page is in the wrong position based on ordering rules.

    Args:
        page: The page to check.
        pos_of_page: The current position of the page in the update list.
        update: A list representing the current order of pages.
        page_ordering_rules: A dictionary where keys are pages and values are lists
            of pages that must precede the key page.

    Returns:
        bool: True if the page is in the wrong position according to the rules,
        False otherwise.
    """
    if page in page_ordering_rules:
        for required_page in page_ordering_rules[page]:
            if required_page in update:
                idx = update.index(required_page)
                if idx > pos_of_page:
                    return True
    return False

def get_correct_position(update, rule) -> int:   
    """
    Determine the highest index position of elements from 'rule' found in 'update'.

    Iterates through each element in 'rule' and checks if it exists in 'update'.
    If found, it updates 'max_pos' with the highest index position of the element
    in 'update'.

    Args:
        update (list): The list to search for elements.
        rule (list): The list containing elements to find in 'update'.

    Returns:
        int: The highest index position of any element from 'rule' found in 'update'.
    """
    max_pos = 0
    for previous_page in rule:
        if previous_page in update:
            i = update.index(previous_page)
            max_pos = max(i,max_pos)
    return max_pos

def reorder_and_get_middle(update, page_ordering_rules):
    """
    Reorder pages in the update list according to the page ordering rules and return
    the middle element.

    Iterates through the update list, checking if each page is in the wrong position
    using the page ordering rules. If a page is misplaced, it is moved to the correct
    position. Finally, the function calculates and returns the middle element of the
    reordered list.

    Args:
        update (list): The list of pages to be reordered.
        page_ordering_rules (dict): A dictionary where keys are pages and values are
            lists of pages that must precede the key page.

    Returns:
        int: The middle element of the reordered update list.
    """
    i = 0
    while i < len(update):
        page = update[i]
        if is_page_in_wrong_position(page, i, update, page_ordering_rules):
            new_idx = get_correct_position(update, page_ordering_rules[page])
            update.insert(new_idx, update.pop(i))
        else:
            i += 1
    middle = get_middle_index(update)
    return int(update[middle])

def main():
    """ Main function
        Reads the specified input file
        Processes the updates for part 1 and part 2
        Prints the results
    """
    file_name = get_file_name()
    file_data = read_input(file_name)
    page_ordering_rules = get_rules(file_data)
    page_updates  = get_updates(file_data)
    answers = get_sum_of_valid_updates(page_updates,page_ordering_rules)
    part_1 = answers[0]
    print(f"Part 1 for {file_name} = {part_1}")
    part_2 = answers[1]
    print(f"Part 2 for {file_name} = {part_2}")

if __name__ == "__main__":
    main()
