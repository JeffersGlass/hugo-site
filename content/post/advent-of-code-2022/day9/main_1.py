from typing import NamedTuple
import sys

class Point(NamedTuple):
    x: int
    y: int

direction_to_vector = {
    "R": Point(1, 0),
    "L": Point(-1, 0),
    "U": Point(0, 1),
    "D": Point(0, -1),
}

def solve_9_1(data):
    head = Point(0, 0)
    tail = Point(0, 0)
    tail_visited = {tail}

    for line in data.split('\n'):
        direction, quantity = line.split(" ")
        diff = direction_to_vector[direction]
        for _ in range(int(quantity)):
            prev_head = head
            head = Point(head.x + diff.x, head.y + diff.y)
            if too_far_9_1(head, tail):
                tail = prev_head
                tail_visited.add(tail)

    return len(tail_visited)

def too_far_9_1(head, tail):
    return abs(head.x - tail.x) > 1 or abs(head.y - tail.y) > 1

if 'pyodide' in sys.modules:
    pass
elif __name__ == '__main__':
    with open ("input.txt", "r") as fp:
        data = fp.read()

    print(f"{solve_9_1(data)}")

