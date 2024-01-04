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
from itertools import combinations
import re
import sys

@dataclass(frozen=True, slots=True)
class Stone:
    x: int
    y: int
    z: int
    vx: int
    vy: int
    vz: int
    slope_2d:int = None

def sign(x):
    if x == 0: return 0
    return abs(x)/x

def main_day24_1(*args):
    data = get_input("day24_1").split("\n")

    pattern = r"(-?\d+),\s+(-?\d+),\s+(-?\d+) @\s+(-?\d+),\s+(-?\d+),\s+(-?\d+)"

    stone_data = (re.match(pattern, line) for line in data)
    stones = [Stone(x=int(m.group(1)),
                    y=int(m.group(2)),
                    z=int(m.group(3)),
                    vx=int(m.group(4)),
                    vy=int(m.group(5)),
                    vz=int(m.group(6)),
                    slope_2d=int(m.group(5))/int(m.group(4)))
                    for m in stone_data]
    
    count = 0
    bounds = (200000000000000, 400000000000000)
    for a, b in combinations(stones, 2):
        if a.slope_2d == b.slope_2d: continue # parallel
        x_cross = (a.slope_2d * a.x - b.slope_2d * b.x - a.y + b.y) / (a.slope_2d - b.slope_2d)
        y_cross = a.slope_2d * (x_cross - a.x) + a.y
        if bounds[0] <= x_cross <= bounds[1] and bounds[0] <= y_cross <= bounds[1] and \
            sign(x_cross - a.x) == sign(a.vx) and sign(x_cross - b.x) == sign(b.vx):
            count += 1

    display(count, target="day24_1-output")

if not 'js' in sys.modules:
    main_day24_1()
