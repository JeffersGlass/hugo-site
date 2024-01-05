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

from copy import deepcopy
from itertools import pairwise      
import sys

def rollNorth(data: str) -> str:
    pattern = [list(line) for line in data.split("\n")]
    for first, second in pairwise(pattern):
        for char_index in range(len(first)):
            if first[char_index] == '.' and second[char_index] == 'O':
                first[char_index] = 'O'
                second[char_index] = '.'
    
    return '\n'.join(''.join(line) for line in pattern)

def main_day14_1(*args):
    data = get_input("day14_1")

    new_data = rollNorth(deepcopy(data))
    while any(new_data[i][j] != data[i][j] for i in range(len(data)) for j in range(len(data[i]))):
        data = deepcopy(new_data)
        new_data = rollNorth(deepcopy(data))

    load = 0
    for row_index, row in enumerate(new_data.split("\n")):
        row_value = len(new_data.split("\n")) - row_index
        print(f"{row_value}")
        for char in row:
            if char == 'O': load += row_value

    result = load
    display(result, target="day14_1-output")

if not 'js' in sys.modules:
    main_day14_1()
