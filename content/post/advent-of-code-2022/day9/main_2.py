from typing import NamedTuple, Iterable
import sys
import itertools

class Point(NamedTuple):
    x: int
    y: int
    previous: any

class Vector(NamedTuple):
    x: int
    y: int

direction_to_vector = {
    "R": Vector(1, 0),
    "L": Vector(-1, 0),
    "U": Vector(0, 1),
    "D": Vector(0, -1),
}

def pairs(i: Iterable):
    a, b = itertools.tee(i)
    next(b, None)
    return zip(a,b)

def solve_9_2(data):
    head = Point(0, 0, Vector(0, 0))
    tails = [Point(0,0, Vector(0, 0)) for _ in range(9)]
    tail_visited = {(tails[-1].x, tails[-1].y)}

    for line in data.split('\n'):
        #print(f"\n{line=}")
        direction, quantity = line.split(" ")
        head_move = direction_to_vector[direction]

        for _ in range(int(quantity)):
            #print(f"Segments:  {''.join([f'({str(s.x): >2},{str(s.y): >2})' for s in [head, *tails]])}")
            head = Point(x = head.x + head_move.x, y = head.y + head_move.y, previous=Point(head.x, head.y, None))
            #print(f"Head moves by ({head_move.x},{head_move.y}) to ({head.x}, {head.y})")

            #move first tail
            diff =  catchup_step(head, tails[0])
            tails[0] = Point(tails[0].x + diff.x, tails[0].y + diff.y, Vector(tails[0].x, tails[0].y))

            #Move other tails
            for index, following_tail in enumerate(tails[1:]):
                local_index = index + 1
                diff =  catchup_step(tails[local_index-1], following_tail)
                #print(f'Moving tail at index {local_index} by {diff}')
                #print(f"({str(diff.x): >2},{str(diff.y): >2})", end = "")
                tails[local_index] = Point(following_tail.x + diff.x, following_tail.y + diff.y, Point(following_tail.x, following_tail.y, None))

            tail_visited.add((tails[-1].x, tails[-1].y))
            #print(f"Segments:  {''.join([f'({str(s.x): >2},{str(s.y): >2})' for s in [head, *tails]])}")
            #print("")
        
        #input("")

    return len(tail_visited)

def catchup_step(head: Point, tail: Point) -> Vector:
    if abs(head.x - tail.x) > 1 or abs(head.y - tail.y) > 1:
        xdiff = 0
        ydiff = 0
        
        if head.x > tail.x:
            xdiff = 1
        elif head.x < tail.x:
            xdiff = -1
        
        if head.y > tail.y:
            ydiff = 1
        elif head.y < tail.y:
            ydiff = -1

        return Vector(xdiff, ydiff)
        
    return Vector(0, 0)

def test_catchup_step():
    #Identity
    zero_vector = Vector(0, 0)
    a = Vector(x = 0, y = 0)
    assert catchup_step(a, zero_vector) == Vector(0, 0)

    #1 off
    for x in range(-1, 1+1):
        for y in range(-1, 1+1):
            assert catchup_step(Vector(x, y), zero_vector) == Vector(0, 0)

    #2 off
    a = Vector(x = 2, y = 0)
    assert catchup_step(a, zero_vector) == Vector(1, 0)

    a = Vector(x = -2, y = 0)
    assert catchup_step(a, zero_vector) == Vector(-1, 0)

    a = Vector(x = 0, y = 2)
    assert catchup_step(a, zero_vector) == Vector(0, 1)

    a = Vector(x = 0, y = -2)
    assert catchup_step(a, zero_vector) == Vector(0, -1)

    #2, 1 off
    a = Vector(x = 2, y = 1)
    #print(c:= catchup_step(a, zero_vector))
    assert catchup_step(a, zero_vector) == Vector(1, 1)

    a = Vector(x = 2, y = -1)
    assert catchup_step(a, zero_vector) == Vector(1, -1)

    a = Vector(x = -2, y = 1)
    assert catchup_step(a, zero_vector) == Vector(-1, 1)

    a = Vector(x = -2, y = -1)
    assert catchup_step(a, zero_vector) == Vector(-1, -1)

    a = Vector(x = 1, y = 2)
    #print(c:= catchup_step(a, zero_vector))
    assert catchup_step(a, zero_vector) == Vector(1, 1)

    a = Vector(x = 1, y = -2)
    assert catchup_step(a, zero_vector) == Vector(1, -1)

    a = Vector(x = -1, y = 2)
    assert catchup_step(a, zero_vector) == Vector(-1, 1)

    a = Vector(x = -1, y = -2)
    assert catchup_step(a, zero_vector) == Vector(-1, -1)

    # 2, 2 off
    a = Vector(x = 2, y = 2)
    assert catchup_step(a, zero_vector) == Vector(1, 1)

    a = Vector(x = -2, y = 2)
    assert catchup_step(a, zero_vector) == Vector(-1, 1)

    a = Vector(x = 2, y = -2)
    assert catchup_step(a, zero_vector) == Vector(1, -1)

    a = Vector(x = -2, y = -2)
    assert catchup_step(a, zero_vector) == Vector(-1, -1)

    print("Tests pass")

if 'pyodide' in sys.modules:
    pass
elif __name__ == '__main__':
    with open ("input.txt", "r") as fp:
        data = fp.read()

    print(f"{solve_9_2(data)}")

    #test_catchup_step()

    

