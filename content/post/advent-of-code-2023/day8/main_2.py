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
from math import prod, lcm
import re

@dataclass
class Instruction:
    left: str
    right: str

def main_day8_2(*args):
    data = get_input("day8_2").split("\n")

    pattern = re.compile(r"([A-Z0-9]{3}) = \(([A-Z0-9]{3}), ([A-Z0-9]{3})\)")

    turns = cycle(data[0].strip())
    node_data = {re.match(pattern, line).group(1):
                 Instruction(left=m.group(2), right=m.group(3)) for line in data[2:] if (m := re.match(pattern, line))}
    
    steps = 0
    ghosts = [loc for loc in node_data.keys() if loc.endswith('A')]
    periods = [-1 for _ in range(len(ghosts))]
    print(ghosts)

    while(True):
        if all(p != -1 for p in periods): break
        direction = next(turns)

        for index, ghost in enumerate(ghosts):
            if ghost.endswith("Z"): periods[index] = steps
            next_step = node_data[ghost]
            #print(f"{ghost=} {next_step=} {direction}") 
            if direction == 'L': ghosts[index] = next_step.left
            elif direction == 'R': ghosts[index] = next_step.right
            else: raise ValueError("Direction must be L or R")

        steps+=1
        #print(ghosts)

    print(periods)
    result = lcm(*periods)
    display(result, target="day8_2-output")

try:
    import js
except ImportError:
    main_day8_2()