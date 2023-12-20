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

import bisect
from dataclasses import dataclass                
import sys
from typing import Iterable

RIGHT = (0, 1)
LEFT = (0, -1)
UP = (-1, 0)
DOWN = (1, 0)

@dataclass
class Header:
    location: tuple[int, int]
    direction: tuple[int, int]
    total_length: int
    moves_this_dir: int = 0

def getNewHeaders(Header, data) -> Iterable[Header]:
    pass # TODO maybe this is the wrong algorithm....



def main_day17_1(*args):
    inp = get_input("day17_1").split("\n")
    data = {(line_index, char): value for line_index, line in enumerate(inp) for char, value in enumerate(line)}

    headers = [Header((0,0), RIGHT, 0),
               Header((0,0), DOWN, 0)]
    
    while True:
        pass # TODO 

    result = None
    display(result, target="day17_1-output")

if not 'js' in sys.modules:
    main_day17_1()
