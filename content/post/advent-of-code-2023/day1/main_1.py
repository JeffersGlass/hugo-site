from pyscript import display
from utils import get_input

import re

def main_day1_1(*args):
    data = get_input("day1_1").split("\n")
    
    sum = 0
    pattern = re.compile("[a-zA-Z]*(?P<first>\d)\w*(?P<last>\d)[a-zA-Z]*")
    single_digit_pattern = re.compile("[a-zA-Z]*(?P<first>\d)\w*")

    for line in data:
        match = re.match(pattern, line)
        if not match: match = re.match(single_digit_pattern, line)
        number = 10 * (first:= int(match.group("first"))) + (int(match.group("last")) if "last" in match.groupdict() else int(first))
        sum += number

    display(sum, target="day1_1-output")     