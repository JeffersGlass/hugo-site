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

import sys
from typing import List

def main_day10_1(*args):
    data: List[str] = get_input("day10_1").split('\n')
    
    _pos_y, _start_line = [(index, line )for index, line in enumerate(data) if 'S' in line][0]
    _pos_x = _start_line.index('S')
    print(f"{_pos_y=}, {_pos_x=}")

    result = None
    display(result, target="day10_1-output")

if not 'js' in sys.modules:
    main_day10_1()
