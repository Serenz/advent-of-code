"""
    Source of the challege:
    https://adventofcode.com/2023/day/1

    Second part of the challenge:
    https://adventofcode.com/2023/day/1#part2
"""

import re

english_numbers = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}


def find_digit(text):
    match = re.search(r'\d', text)
    return match.group()


def find_digit2(text):
    pattern = r'\d|' + '|'.join(english_numbers.keys())
    match = re.findall(pattern, text)
    first, last = match[0], match[-1]
    first = english_numbers.get(first, first)
    last = english_numbers.get(last, last)
    return first + last

if __name__ == '__main__':
    with open('day1_input.txt', 'r') as f:
        strings = f.readlines()
    solution = 0
    for string in strings:
        # s_number = find_digit(string) + find_digit(string[::-1])      This is for the first part of the challenge
        s_number = find_digit2(string)
        solution += int(s_number)
    print(solution)