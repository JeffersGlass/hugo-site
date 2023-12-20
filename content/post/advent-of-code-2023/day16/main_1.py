try:
    from pyscript import document
    from utils import get_input
except ImportError:
    def get_input(*args):
        with open("input_test.txt") as f:
            return f.read()
        
    def display(*args, **kwargs):
        if 'target' in kwargs:
            kwargs.pop('target')
        print(*args, **kwargs)
                
from enum import Enum
import sys
from typing import Iterable

class Dir(Enum):
    LEFT = (0, -1)
    RIGHT = (0, 1)
    UP = (-1, 0)
    DOWN = (1, 0)

def get_next_tile(coords: Iterable[int, int], direction: Dir, value: str, dims: Iterable[int, int]) -> Iterable[Iterable[int, int]]:
    # Off edge of map
    if coords[0] < 0 or coords [0] >= dims[0] or \
        coords[1] < 0 or coords [1] >= dims[1]:
        return []

    # Move through empty space and parallel splitters
    if value == '.' or \
        (direction in (Dir.LEFT, Dir.RIGHT) and value == '-') or \
        (direction in (Dir.UP, Dir.DOWN) and value == "|"):
        return [(coords[0] + direction[0], coords[1] + direction[1])]
    
    # Vertical Splitter
    if direction in (Dir.LEFT, Dir.RIGHT) and value == "|":
        return [(coords[0]-1, coords[1]), (coords[0]+1, coords[1])]
    

    # Horizontal Splitter
    if direction in (Dir.UP, Dir.DOWN) and value == "-":
        return [(coords[0], coords[1]-1), (coords[0], coords[1]+1)]
    
    # TODO bouncing mirrors
    #if (direction == Dir.RIGHT and value == "\")...
    
    raise ValueError("Unhandled Instruction")   

def main_day16_1(*args):
    data = {(line, char): value for line in get_input("day16_1").split("n") for char, value in enumerate(line)}

    result = None
    display(result, target="day16_1-output")

if not 'js' in sys.modules:
    main_day16_1()
