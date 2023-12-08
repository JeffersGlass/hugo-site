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

from dataclasses import dataclass
from itertools import cycle
import re

@dataclass
class Instruction:
    left: str
    right: str

def main_day8_1(*args):
    data = get_input("day8_1").split("\n")

    pattern = re.compile(r"([A-Z]{3}) = \(([A-Z]{3}), ([A-Z]{3})\)")

    turns = cycle(data[0].strip())
    node_data = {re.match(pattern, line).group(1):
                 Instruction(left=m.group(2), right=m.group(3)) for line in data[2:] if (m := re.match(pattern, line))}
    
    steps = 0
    loc = 'AAA'

    while(True):
        if loc == 'ZZZ': break
        next_step = node_data[loc]
        direction = next(turns)
        if direction == 'L': loc = next_step.left
        elif direction == 'R': loc = next_step.right
        else: raise ValueError("Direction must be L or R")

        steps+=1

    result = steps
    display(result, target="day8_1-output")

try:
    import js
except ImportError:
    main_day8_1()