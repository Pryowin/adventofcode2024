""" 
Day 2 of Advent of Code 2024
https://adventofcode.com/2024/day/2
"""
import os
import sys

DEFAULT_FILE_NAME = "input.txt"



def read_input(file_name:str) -> list:
    """Read input file

    Args:
        file_name (str): Name of the input file
        File is in same location as the python code
        
    Returns:
        A list of the lines in the file
    """
    reports = []
    file = os.path.join(os.path.dirname(__file__), file_name)
    with open(file, encoding="utf-8") as input_data:
        for line in input_data:
            reports.append(line)
    return reports


def count_safe(reports:list,is_first_problem:bool) -> int: 
    """
    Counts the number of safe reports based on the specified safety criteria.

    Iterates through a list of reports and determines if each report is safe
    using either the basic safety check or the dampened safety check, depending
    on the value of `is_first_problem`.

    Args:
        reports (list): A list of report strings to be evaluated.
        is_first_problem (bool): A flag indicating which safety check to use.
            If True, uses the basic safety check; otherwise, uses the dampened
            safety check.

    Returns:
        int: The count of reports that are considered safe.
    """
    safety_count = 0
    for report in reports:
        if is_first_problem:
            if is_safe(report):
                safety_count += 1
        else:
            if is_safe_with_dampener(report):
                safety_count +=1
    return safety_count

def is_safe(report) -> bool:
    """
    Determines if the levels in the report are safe based on their order and difference.

    The function checks if the sequence of levels, derived from the report string, 
    is either strictly ascending or descending with each step differing by 1 to 3 units.

    Args:
        report (str): A string containing space-separated level values.

    Returns:
        bool: True if the levels are safe, False otherwise.
    """
    levels =  [int(n) for n in report.split()]
    ascending = True
    if levels[0] > levels[1]:
        ascending = False
    for i in range(0, len(levels)-1):
        if ascending:
            if not levels[i+1] - levels[i] in range(1,4):
                return False
        else:
            if not levels[i] - levels[i+1] in range(1,4):
                return False
    return True

def is_safe_with_dampener(report) -> bool:
    """
    Determines if the levels in the report are safe, allowing for one level to be removed.
    This function first checks if the levels in the report are safe using the is_safe
    function.
    If not, it attempts to remove each level one by one and checks again if the remaining levels
    are safe. The levels are considered safe if they are strictly ascending or descending with
    each step differing by 1 to 3 units.

    Args:
    report (str): A string containing space-separated level values.

    Returns:
    bool: True if the levels are safe or can be made safe by removing one level, False otherwise.

    """
    if is_safe(report):
        return True
    levels =  [int(n) for n in report.split()]
    for i in range(0, len(levels)):
        levels_clone = [int(n) for n in report.split()]
        del levels_clone[i]
        changed_report = ' '.join(str(item) for item in levels_clone)
        if is_safe(changed_report):
            return True
    return False

def get_file_name() -> str:
    """ Returns the base file name for the input to problem
    Return: If no args were provided when program was run, returns the default
    Otherwise it returns the file name provided on the command line
    """
    if len(sys.argv) == 1:
        return DEFAULT_FILE_NAME
    return sys.argv[1]

def main():
    """ Main function
        Reads the specified input file
        Runs the Safety Count
        Once with the original rules
        Once with the rules for the second part 
    """
    file_name = get_file_name()
    reports = read_input(file_name)
    print(count_safe(reports,True))
    print(count_safe(reports,False))

if __name__ == "__main__":
    main()
