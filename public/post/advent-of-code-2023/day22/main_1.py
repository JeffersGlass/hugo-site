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

from dataclasses import dataclass, field
from collections import namedtuple
from itertools import permutations
import re
import sys
from typing import Self

Point = namedtuple("Point", ['x', 'y', 'z'])

def point_under(p: Point) -> Point:
    return Point(p.x, p.y, p.z -1)

def point_above(p:Point) -> Point:
    return Point(p.x, p.y, p.z+1)

@dataclass(slots=True)
class Brick:
    cells: set[Point]
    vertical: bool = False
    supported_by: list[Self] = field(default_factory=list)
    
    @property
    def footprint(self) -> set[Point]:
        if self.vertical:
            cell = next(iter(self.cells))
            x = cell.x
            y = cell.y
            z = min(p.z for p in self.cells)
            return set([Point(x, y, z)])
        return self.cells # If not vertical, footprint is self
    

bricks: list[Brick] = list()

def brick_in(loc: tuple[int, int, int], bricks: set[Brick], current_brick=None) -> Brick | None:
    for b in bricks:
        if loc in b.cells: return b
    return None
    if (length:= len(matches:= [b for b in bricks if loc in b.cells])) == 1: 
        if matches[0] == current_brick: raise ValueError("Somehow comapring to current brick")
        return matches[0]
    if length > 1: raise ValueError(f"Detected more than one brick in cell {loc}: {matches}")
    return None

def main_day22_1(*args):
    data = reversed(get_input("day22_1").split("\n"))

    for line in data:
        m = re.match(r"(\d+),(\d+),(\d+)~(\d+),(\d+),(\d+)", line)
        x1, x2 = int(m.group(1)), int(m.group(4))
        x1, x2 = min(x1, x2), max(x1, x2)
        y1, y2 = int(m.group(2)), int(m.group(5))
        y1, y2 = min(y1, y2), max(y1, y2)
        z1, z2 = int(m.group(3)), int(m.group(6))
        z1, z2 = min(z1, z2), max(z1, z2)
        if x1 != x2: # Along X direction
            bricks.append(Brick(set(Point(x, y1, z1) for x in range(x1, x2+1))))
        elif m.group(2) != m.group(5): # Along y direction
            bricks.append(Brick(set(Point(x1, y, z1) for y in range(y1, y2+1))))
        elif m.group(3) != m.group(6): # Along z direction
            bricks.append(Brick(set(Point(x1, y1, z) for z in range(z1, z2+1)), vertical=True))
            
        else:
            bricks.append(Brick(set([Point(x1, y1, z1),])))

    print("Bricks created")

    # Let bricks fall down
    anything_moved = True
    while anything_moved:
        anything_moved = False
        for index, b in enumerate(bricks):
            stationary = False
            for cell in b.footprint:
                if cell.z == 1: # on ground
                    stationary = True; break
                if x:= brick_in(point_under(cell), bricks, b): # space underneath is occupied
                    stationary = True; break

            if not stationary:
                bricks[index] = Brick(set(Point(c.x, c.y, c.z-1) for c in b.cells), vertical=b.vertical)
                anything_moved = True

    print("Bricks have fallen")

    #calculate supporting bricks for all bricks
    for b in bricks:
        b.supported_by = [brick_in(point_under(c), bricks) for c in b.footprint if brick_in(point_under(c), bricks) is not None]

    for index, b in enumerate(bricks):
        if b.supported_by:
            print(f"Brick {index} is supported by bricks {','.join(str(bricks.index(c)) for c in b.supported_by)}")
        else: print(f"Brick {index} is not supported by any other bricks")
    

    removable_bricks = 0
    for a_index, a in enumerate(bricks):
        a_removable = True
        for b in bricks:
            if a == b: continue
            if b.supported_by and a in b.supported_by and len(b.supported_by) == 1:
                a_removable = False
                break
        if a_removable: 
            removable_bricks += 1
        

    print(f"{(removable_bricks)=}")
    #711 was too high
        

    result = None
    display(result, target="day22_1-output")

if not 'js' in sys.modules:
    main_day22_1()
