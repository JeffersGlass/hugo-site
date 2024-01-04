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

from collections import deque
from dataclasses import dataclass
from itertools import pairwise
import re    
import sys

@dataclass(frozen=True)
class Location:
    x: int
    y: int

inst = {
    "R": Location(x = 1, y = 0),
    "L": Location(x = -1, y = 0),
    "U": Location(x = 0, y = -1),
    "D": Location(x = 0, y = 1)
}

def score_shoelace(trench, length):
    for (one, two) in pairwise(trench):
        print(one, two)
    return .5 * sum((one.x * two.y) - (two.x * one.y) for (one, two) in pairwise(trench)) + .5 * length + 1

def get_trench_2(data):
    loc = Location(x = 0, y = 0)
    trench = [Location(0,0)]
    length = 0 

    for line in data:
        m = re.search(r"(?P<num>[0-9a-f]{5})(?P<dir>[0-3])", line)
        num = int(m.group("num"), base=16)
        dir = str.translate(m.group("dir"), str.maketrans("0123", "RDLU"))
        loc = Location(loc.x + (inst[dir].x * num), loc.y + (inst[dir].y * num))
        length += num
        trench.append(loc)
    assert loc == Location(0,0)
    return trench, length

def main_day18_2(*args):
    data = get_input("day18_2").split('\n')

    result = score_shoelace(*get_trench_2(data))

    display(result, target="day18_2-output")

if not 'js' in sys.modules:
    main_day18_2()
