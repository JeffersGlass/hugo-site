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
                

import sys

def hash(s: str) -> int:
    value = 0
    for char in s:
        value += ord(char)
        value *= 17
        value %= 256
    return value

def main_day15_1(*args):
    data = get_input("day15_1")

    result = sum(hash(s) for s in data.split(','))
    display(result, target="day15_1-output")

if not 'js' in sys.modules:
    main_day15_1()
