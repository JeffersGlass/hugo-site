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
from itertools import pairwise, count      
import sys
from typing import List, Callable

def cycle(data: str) -> str:
    data = completely(data, rollNorth)
    data = completely(data, rollWest)
    data = completely(data, rollSouth)
    return completely(data, rollEast)

def completely(data: str, f: [str, str]) -> str:
    #print(f"Applying function {f.__name__} completly")
    new_data = f(deepcopy(data))
    while any(new_data[i][j] != data[i][j] for i in range(len(data)) for j in range(len(data[i]))):
        data = deepcopy(new_data)
        new_data = f(deepcopy(data))
    return new_data

def rollNorth(data: str) -> str:
    pattern = [list(line) for line in data.split("\n")]
    for first, second in pairwise(pattern):
        for char_index in range(len(first)):
            if first[char_index] == '.' and second[char_index] == 'O':
                first[char_index] = 'O'
                second[char_index] = '.'
    
    return '\n'.join(''.join(line) for line in pattern)

def rollSouth(data: str) -> str:
    pattern = [list(line) for line in data.split("\n")]
    for first, second in pairwise(reversed(pattern)):
        for char_index in range(len(first)):
            if first[char_index] == '.' and second[char_index] == 'O':
                first[char_index] = 'O'
                second[char_index] = '.'
    
    return '\n'.join(''.join(line) for line in pattern)

def rollEast(data:str) -> str:
    pattern = [list(line) for line in data.split("\n")]
    for first_index, second_index in pairwise(range(len(pattern[0]))):
        for line in pattern:
            if line[second_index] == '.' and line[first_index] == 'O':
                line[second_index] = 'O'
                line[first_index] = '.'

    return '\n'.join(''.join(line) for line in pattern)

def rollWest(data:str) -> str:
    pattern = [list(line) for line in data.split("\n")]
    for first_index, second_index in pairwise(reversed(range(len(pattern[0])))):
        for line in pattern:
            if line[second_index] == '.' and line[first_index] == 'O':
                line[second_index] = 'O'
                line[first_index] = '.'

    return '\n'.join(''.join(line) for line in pattern)

def print_pattern(data:str):
    for line in data.split("\n"):
        print(line)

def main_day14_2(*args):
    data = get_input("day14_2")
    configs = []

    counter = count()
    while data not in configs:
        print(loop_point:= counter.__next__())
        configs.append(data)
        data = cycle(data)

    first_occurance = configs.index(data)
    print(f"{first_occurance=}")
    print(f"{loop_point=}")
    loop_length = loop_point - first_occurance

    # TODO: Given the two points of repetition, calculate
    # the value after 1_000_000_000 cycles

    print_pattern(configs[first_occurance])
    print("")
    print_pattern(configs[loop_point])


        
        

    load = 0
    for row_index, row in enumerate(data.split("\n")):
        row_value = len(data.split("\n")) - row_index
        for char in row:
            if char == 'O': load += row_value

    result = load
    display(result, target="day14_2-output")

if not 'js' in sys.modules:
    main_day14_2()
