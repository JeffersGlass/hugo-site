from pyscript import display
from utils import get_input

import re

patterns = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    }

digit_pattern = re.compile('\d')

def get_value(s):
    try:
        return int(s)
    except ValueError:
        return patterns[s]

def main_day1_2(*args):
    data = get_input("day1_2").split("\n")

    sum = 0
    
    for line in data:
        line_matches = []

        for pattern in patterns:
            line_matches.extend(re.finditer(pattern, line))

        line_matches.extend(re.finditer(digit_pattern, line))
        line_matches.sort(key = lambda m: m.start())
        sum += 10 * get_value(line_matches[0].group(0)) + get_value(line_matches[-1].group(0))

    display(sum, target="day1_2-output")  

if __name__ == "__main__":
    try:
        import js
    except ImportError:
        main_day1_2()