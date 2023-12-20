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
import rich
import sys
from typing import Iterable


LEFT = (0, -1)
RIGHT = (0, 1)
UP = (-1, 0)
DOWN = (1, 0)

def get_next_tiles(coords: tuple[int, int], direction: tuple[int, int], data, dims: tuple[int, int]) -> Iterable[tuple[int, int]]:
    # Off edge of map
    if coords[0] < 0 or coords [0] >= dims[0] or \
        coords[1] < 0 or coords [1] >= dims[1]:
        return set()
    
    value = data[(coords[0], coords[1])]

    # Move through empty space and parallel splitters
    if value == '.' or \
        (direction in (LEFT, RIGHT) and value == '-') or \
        (direction in (UP, DOWN) and value == "|"):
        return [((coords[0] + direction[0], coords[1] + direction[1]), direction)]
    
    # Vertical Splitter
    if direction in (LEFT, RIGHT) and value == "|":
        return [((coords[0]-1, coords[1]), UP),
                 ((coords[0]+1, coords[1]), DOWN)]
    

    # Horizontal Splitter
    if direction in (UP, DOWN) and value == "-":
        return [((coords[0], coords[1]-1), LEFT),
                 ((coords[0], coords[1]+1), RIGHT)]
    
    # Bouncing Down
    if (direction == RIGHT and value == "\\") or \
        (direction == LEFT and value == "/"):
        return [((coords[0] + 1, coords[1]), DOWN)]
    
    # Bouncing Up
    if (direction == RIGHT and value == "/") or \
        (direction == LEFT and value == "\\"):
        return [((coords[0] - 1 , coords[1]), UP)]
    
    # Bouncing Left
    if (direction == DOWN and value == "/") or \
        (direction == UP and value == "\\"):
        return [((coords[0], coords[1] - 1), LEFT)]
    
    # Bouncing Right
    if (direction == DOWN and value == "\\") or \
        (direction == UP and value == "/"):
        return [((coords[0], coords[1] + 1), RIGHT)]
    
    raise ValueError("Unhandled Instruction")   

def printGrid(lasers, inp, illuminated_spaces):
    for line_index, line in enumerate(inp):
        for char_index, char in enumerate(line):
            lasers_here = [(laser[0][0], laser[0][1]) for laser in lasers if laser[0][0] == line_index and laser[0][1] == char_index]
            if lasers_here:
                rich.print('[red]X[/red]', end="")
            elif (line_index, char_index) in illuminated_spaces:
                rich.print(f'[blue]#[/blue]', end="")
            else: print(char, end = "")
        print("")

def score_16_2(start_space: tuple[int, int], start_dir: tuple[int, int], inp) -> int:
    data = {(line_index, char): value for line_index, line in enumerate(inp) for char, value in enumerate(line)}

    lasers = set([(start_space, start_dir),])
    illuminated_spaces = set([start_space,])
    old_lasers = set()

    dims = (len(inp), len(inp[0]))

    while lasers:
        new_lasers = set()
        for laser in lasers:
            new_lasers |= set(get_next_tiles(laser[0], laser[1], data, dims))
        if new_lasers <= old_lasers: break
        old_lasers |= new_lasers
        lasers = new_lasers
        illuminated_spaces = illuminated_spaces.union(set((laser[0][0], laser[0][1]) for laser in lasers))

    return len([s for s in illuminated_spaces if (0 <= s[0] < dims[0]) and (0 <= s[1] < dims[1])])

def main_day16_2(*args):
    inp = get_input("day16_2").split("\n")
    max_score = -1

    # Left and Right Sides
    for i in range(len(inp)):
        max_score = max(max_score, score_16_2((i, 0), RIGHT, inp))
        max_score = max(max_score, score_16_2((i, len(inp[0])-1), LEFT, inp))

    # Top and Bottom
    for i in range(len(inp[0])):
        max_score = max(max_score, score_16_2((0, i), DOWN, inp))
        max_score = max(max_score, score_16_2((len(inp)-1, i), UP, inp))
    
    display(max_score, target="day16_2-output")

if not 'js' in sys.modules:
    main_day16_2()
