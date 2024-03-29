try:
    from pyscript import document
    from utils import get_input
except ImportError:
    def get_input(*args):
        with open("input.txt") as f:
            return f.read()
        
    def display(*args, **kwargs):
        if 'target' in kwargs:
            kwargs.pop('target')
        print(*args, **kwargs)

import re

card_pattern = re.compile("Card (\d+)")
number_pattern = re.compile("\d+")

def main_day4_1(*args):
    data = get_input("day4_1").split('\n')

    sum = 0
    for line in data:
        _, numbers_section = line.split(":")
        winning_numbers = set(m.group(0) for m in re.finditer(number_pattern, numbers_section.split("|")[0]))
        my_numbers = set(m.group(0) for m in re.finditer(number_pattern, numbers_section.split("|")[1]))
        value = 0 if winning_numbers.isdisjoint(my_numbers) else 2 ** (len(winning_numbers & my_numbers) - 1)
        sum += value

    display(sum, target="day4_1-output")

import sys
if not 'js' in sys.modules:
    main_day4_1()
