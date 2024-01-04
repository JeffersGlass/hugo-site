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

def score_shoelace(data):
    loc = Location(x = 0, y = 0)
    trench = [Location(0,0)]

    for line in data:
        m = re.match(r"(?P<dir>[RDLU]) (?P<num>\d)", line)
        dir, num = m.group("dir"), m.group("num")
        for _ in range(int(num)):
            loc = Location(loc.x + inst[dir].x, loc.y + inst[dir].y)
        trench.append(loc)
    
    for (one, two) in pairwise(trench):
        print(one, two)
    return sum((one.x * two.y) - (two.x * one.y) for (one, two) in pairwise(trench))

def get_trench(data):
    loc = Location(x = 0, y = 0)
    trench = set([Location(0,0)])

    for line in data:
        m = re.match(r"(?P<dir>[RDLU]) (?P<num>\d+)", line)
        dir, num = m.group("dir"), m.group("num")
        for _ in range(int(num)):
            loc = Location(loc.x + inst[dir].x, loc.y + inst[dir].y)
            trench.add(loc)
    assert loc == Location(0,0)
    return trench

def score_flood_fill(trench):
    left = min(loc.x for loc in trench)
    right = max(loc.x for loc in trench)
    top = min(loc.y for loc in trench)
    bottom = max(loc.y for loc in trench)

    print(f"{left=} {right=} {top=} {bottom=}")

    nodes = set([Location(left-1, top-1)])
    seen = set(nodes)

    while nodes:
        current = nodes.pop()
        seen.add(current)
        for new_node in (Location(current.x, current.y - 1),
                         Location(current.x, current.y + 1),
                         Location(current.x - 1, current.y),
                         Location(current.x + 1, current.y)):
            if new_node.x >= left - 1 and \
                new_node.x <= right + 1 and \
                new_node.y >= top - 1 and \
                new_node.y <= bottom + 1 and \
                new_node not in trench and \
                new_node not in seen:
                nodes.add(new_node)   
        print(len(nodes))

    with open("viz.txt", "w") as f:
        for y in range(top-1, bottom+2):
            for x in range(left-1, right+2):
                if Location(x, y) in seen: print("#",end = "" , file = f)
                else: print(".", end = "", file = f)
            print("",file = f)

    area = (right-left+3) * (bottom-top+3)
    print(f"Total area: {area=}")
    print(f"Flooded exterior = {len(seen)}")
    print(f"Interior = {area - len(seen)}")


def main_day18_1(*args):
    data = get_input("day18_1").split('\n')

    #result = score_shoelace(data)
    result = score_flood_fill(get_trench(data))

    display(result, target="day18_1-output")

if not 'js' in sys.modules:
    main_day18_1()
