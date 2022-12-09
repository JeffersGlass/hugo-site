from typing import NamedTuple
import sys

class Vector(NamedTuple):
    x: int
    y: int

direction_to_vector = {
    "R": Vector(1, 0),
    "L": Vector(-1, 0),
    "U": Vector(0, 1),
    "D": Vector(0, -1),
}

def solve_9_1(data):
    head = Vector(0, 0)
    tail = Vector(0, 0)
    tail_visited = {tail}

    for line in data.split('\n'):
        direction, quantity = line.split(" ")
        diff = direction_to_vector[direction]
        for _ in range(int(quantity)):
            prev_head = head
            head = Vector(head.x + diff.x, head.y + diff.y)
            if too_far_9_1(head, tail):
                tail = prev_head
                tail_visited.add(tail)

    return len(tail_visited)

def too_far_9_1(head, tail):
    return abs(head.x - tail.x) > 1 or abs(head.y - tail.y) > 1

if 'pyodide' in sys.modules:
    def main_day9_1():
        data = get_input('day9_1')
        display(f"{solve_9_1(data)=}",
            target="day9_1-output",
            append=False)
elif __name__ == '__main__':
    with open ("input.txt", "r") as fp:
        data = fp.read()

    print(f"{solve_9_1(data)}")