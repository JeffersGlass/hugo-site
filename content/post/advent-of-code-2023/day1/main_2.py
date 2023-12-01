from pyscript import display
from utils import get_input

import re

def main_day1_2(*args):
    data = get_input("day1_2").split("\n")
    raw_patterns = {
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
        }
    
    digit_pattern = re.compile('\d')
    patterns = {k: re.compile(v) for k,v in raw_patterns.items()}

    sum = 0
    for line in data:
        min_index, min_value = float('inf'), None
        max_index, max_value = -1, None

        # Deal with spelled-out numbers
        for p_value in patterns:
            matches = list(re.finditer(patterns[p_value], line))
            if matches:
                lowest_index = min(match.start() for match in matches)
                if lowest_index < min_index: min_index, min_value = lowest_index, p_value

                highest_index = max(match.start() for match in matches)
                if highest_index > max_index: max_index, max_value = highest_index, p_value

        # Deal with actual raw digits
        matches = list(re.finditer(digit_pattern, line))
        if matches:
            lowest_match = sorted(matches, key = lambda m: m.start())[0]
            if lowest_match.start() < min_index: min_index, min_value = lowest_index, int(lowest_match.group(0))

            highest_match = sorted(matches, key = lambda m: m.start(), reverse=True)[0]
            if highest_match:
                if highest_match.start() > max_index: max_index, max_value = highest_index, int(highest_match.group(0))

        #print(f"{line} : {min_value=} , {max_value=}")

        number = 10 * min_value + (max_value if max_value else min_value)
        #print(f"{number} : {line.strip()}")

        sum += number
    
    display(sum, target="day1_2-output")  