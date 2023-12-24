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

from dataclasses import dataclass
from collections import namedtuple
import re
import sys

Point = namedtuple("Point", ['x', 'y', 'z'])

def point_under(p: Point):
    return Point(p.x, p.y, p.z -1)

@dataclass(frozen=True, slots=True)
class Brick:
    cells: set[Point]
    vertical: bool = False
    
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

def brick_in(loc: tuple[int, int, int], bricks: set[Brick]) -> Brick | None:
    if (length:= len(matches:= [b for b in bricks if loc in b.cells])) == 1: return matches[0]
    if length > 1: raise ValueError(f"Detected more than one brick in cell {loc}: {matches}")
    return None

def main_day22_1(*args):
    data = get_input("day22_1").split("\n")

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

    for b in bricks:
        print(b)

    # Let bricks fall down
    moved = True
    while moved:
        moved = False
        for index, b in enumerate(bricks):
            stationary = False
            for cell in b.footprint:
                if cell.z == 1: # on ground
                    stationary = True; break
                if brick_in(point_under(cell), bricks): # space underneath is occupied
                    stationary = True; break

            if not stationary:
                print(f"Moving brick {b}")
                bricks[index] = Brick(set(Point(c.x, c.y, c.z-1) for c in b.cells))
                moved = True

    # TODO Something in this moving logic is wrong

    print("")
    for b in bricks:
        print(b)

    result = None
    display(result, target="day22_1-output")

if not 'js' in sys.modules:
    main_day22_1()
