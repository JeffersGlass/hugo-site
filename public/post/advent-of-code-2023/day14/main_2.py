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

from itertools import pairwise, count      
import sys

def cycle(data: str) -> str:
    data = completely(data, rollNorth)
    data = completely(data, rollWest)
    data = completely(data, rollSouth)
    return completely(data, rollEast)

def completely(data: str, f: [str, str]) -> str:
    new_data = f(data)
    while new_data != data:
        data = new_data
        new_data = f(data)
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

def get_load(data: str) -> int:
    load = 0
    for row_index, row in enumerate(data.split("\n")):
        row_value = len(data.split("\n")) - row_index
        for char in row:
            if char == 'O': load += row_value
    return load

def main_day14_2(*args):
    data = get_input("day14_2")
    configs = []

    counter = count()
    while data not in configs:
        print(loop_point:= counter.__next__(), "\t", get_load(data) )
        configs.append(data)
        data = cycle(data)

    loop_point += 1
    first_occurance = configs.index(data)
    print(f"After {loop_point=} iterations, the stones were in the same place as after {first_occurance}")
    loop_length = loop_point - first_occurance
    target = 1_000_000_000
    last_loop = (int((target - first_occurance)/loop_length)) * loop_length + first_occurance
    difference = target - last_loop

    for _ in range(difference):
        data = cycle(data)

    result = get_load(data)
    display(result, target="day14_2-output")

if not 'js' in sys.modules:
    main_day14_2()
