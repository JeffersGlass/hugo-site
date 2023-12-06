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

from operator import itemgetter
import re
from typing import Tuple

def almanac_op_range(seed_ranges, dest_start: int, source_start: int, length:int) -> Tuple[Tuple[Tuple[int, int]], Tuple[Tuple[int, int]]]:
    """Given a list of ranges as input, and a single mapping given by a starting
    destination index, starting source index, and length, return a list of ranges
    that have not been touched by this rule and a list of ranges that have been modified
    by this rule

    Args:
        seed_ranges (_type_): _description_
        dest_start (int): _description_
        source_start (int): _description_
        length (int): _description_

    Raises:
        ValueError: A troubleshooting step, to validate that the rules for processing
        ranges cover all possible cases

    Returns:
        List[Tuple[int, int]], List[Tuple[int, int]]: A list of untouched ranges, followe
        by a list of ranges that had been moved
    """
    source_end = source_start + length - 1
    dest_end = dest_start + length - 1

    untouched = []
    moved = []
    for given in seed_ranges:
        given_start, given_end = given[0], given[1]
        #print(f"given = {given_start, given_end}, dest={dest_start, dest_end}, source={source_start, source_end}")

        if given_end < source_start or given_start > source_end: #outside of source range
            untouched.append(given)
        
        elif given_start >= source_start and given_end <= source_end: # given entirely within source range
            moved.append(((given_start - source_start + dest_start), (given_end - source_start + dest_start)))
        
        elif given_start < source_start and given_end > source_end: # given entirely surrounds source range
            untouched.append((given_start, source_start-1))
            untouched.append((source_end + 1, given_end))
            moved.append((dest_start, dest_end))
        
        elif given_start >= source_start and given_end > source_end: # starts is within source, end isn't
            moved.append((given_start - source_start + dest_start,source_end-source_start+dest_start))
            untouched.append((source_end+1, given_end))

        elif given_start < source_start and given_end <= source_end: # starts before source, ends inside
            untouched.append((given_start, source_start -1))
            moved.append((dest_start,given_end-source_start+dest_start))
        else:
            raise ValueError("Should never be here")
        
    return untouched, moved

def main_day5(*args):
    data = get_input("day5_2")

    seed_ranges = [(int(s.group(1)), int(s.group(1)) + int(s.group(2)) - 1) for s in re.finditer(r"(\d+) (\d+)", data.split("\n")[0].split(":")[1])]
    map_sets = [[l.split(" ") for l in s.split('\n')[1:]] for s in data.split("\n\n")][1:]

    untouched = seed_ranges
    for map_set in map_sets:
        moved = []  
        for op in map_set:
            untouched, new_moved = almanac_op_range(untouched, int(op[0]), int(op[1]), int(op[2]))
            moved.extend(new_moved)
            if not untouched: break #If there's no numbers that haven't been mapped, no need to keep processing rules
        untouched.extend(moved)
        untouched = list(set(untouched))

    minimum = min(r[0] for r in untouched)

    display("FINAL:", minimum, target="day5_2-output")

if __name__ == "__main__":
    main_day5()

    # Assertions used during testing, left in for interest
    assert almanac_op_range(((1,5),), 50, 20, 5) == ([(1,5)],[]) #outside of source range
    assert almanac_op_range([(100,105)], 50, 20, 5) == ([(100,105)],[]) #outside of source range
    assert almanac_op_range([(10, 20)], 50, 15, 2) ==  ([(10,14), (17,20)], [(50, 51)]) # given entirely surrounds source range
    assert almanac_op_range([(10, 20)], 50, 5, 30) == ([],[(55, 65)]) # given entirely within source range
    assert almanac_op_range([(10, 20)], 50, 15, 10) == ([(10, 14)], [(50, 55)]) # starts is within source, end isn't
    assert almanac_op_range([(10, 20)], 50, 5, 10) == ([(15, 20)],[(55,59)]) # starts before source, ends inside
