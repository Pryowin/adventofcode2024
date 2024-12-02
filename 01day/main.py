""" 
Day 1 of Advent of Code 2024
https://adventofcode.com/2024/day/1
"""
import os
import sys

left = []
right = []

def read_input(file_name) -> None:
    """
    Read input file
    Data consists of two numbers separated by 3 spaces
    Function loads the numbers into two arrays (left and right)
    """
    file = os.path.join(os.path.dirname(__file__), file_name)
    with open(file, encoding="utf-8") as input_data:
        for line in input_data:
            pair = line.split("   ")
            left.append(int(pair[0]))
            right.append(int(pair[1]))


def calculate_distance() -> int:
    """ Calculates the absolute distance between pairs of numbers
        Distance is the absolute difference between equivalent values
        in the left and right list. 
    Returns:
        int: The sum of the distances
    """
    distance = 0
    left.sort()
    right.sort()
    items = len(left)
    for i in range(0,items):
        delta = abs(left[i]-right[i])
        distance += delta
    return distance

def calculate_similarity() -> int:
    """ Returns the similarity of the two lists
        Similarity is defined as follows:
            For each number in the number in the left list
            count how often that number appears in the right list
            multiply that count by the number

    Returns:
        int: _The sum of the individual similarity scores_
    """
    similarity = 0
    for num in left:
        count = right.count(num)
        similarity += count * num
    return similarity


def main():
    """ Main function
        Reads the specified input file
        Calculates distance     (Part 1 of puzzle)
        Calculates similarity   (Part 2 of puzzle)
    """
    if len(sys.argv) == 1:
        file = "input.txt"
    else:
        file = sys.argv[1]

    read_input(file)
    print(calculate_distance())
    print(calculate_similarity())

if __name__ == "__main__":
    main()
 