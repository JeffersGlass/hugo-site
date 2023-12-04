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

    display(data, target="day4_2-output")

if __name__ == "__main__":
    main_day4_2()
