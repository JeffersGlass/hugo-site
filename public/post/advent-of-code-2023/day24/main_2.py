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

pattern = r"(-?\d+),\s+(-?\d+),\s+(-?\d+) @\s+(-?\d+),\s+(-?\d+),\s+(-?\d+)"
def main_day24_1(*args):
    data = get_input("day24_1").split("\n")

    stone_data = (re.match(pattern, line) for line in data)
    stones = [Stone(x=int(m.group(1)),
                    y=int(m.group(2)),
                    z=int(m.group(3)),
                    vx=int(m.group(4)),
                    vy=int(m.group(5)),
                    vz=int(m.group(6)),
                    slope_2d=int(m.group(5))/int(m.group(4)))
                    for m in stone_data]
    
    # If N is the number of hailstones, we will solve for N+6 Independent
    # Variables - x, y, z, vx, vy, vz for the thrown projectile, 
    # and the N intercept times

    

    
    result = None

    display(result, target="day24_1-output")

if not 'js' in sys.modules:
    main_day24_1()
