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

def main_day4_2(*args):
    data = get_input("day4").split('\n')
    card_counts = [1] * len(data)

    for i, line in enumerate(data):
        _, numbers_section = line.split(":")
        winning_numbers = set(m.group(0) for m in re.finditer(number_pattern, numbers_section.split("|")[0]))
        my_numbers = set(m.group(0) for m in re.finditer(number_pattern, numbers_section.split("|")[1]))
        for m in range(1, len(winning_numbers & my_numbers)+1):
            card_counts[i + m] += card_counts[i]

    display(sum(card_counts), target="day4_2-output")

if __name__ == "__main__":
    main_day4_2()
