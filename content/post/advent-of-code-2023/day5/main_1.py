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

import re
from typing import Tuple

def almanac_op(given: int, dest_start: int, source_start: int, length: int) -> int:
    """Takes an index of a location and applies the specified mapping rule to it

    Args:
        given (int): The starting location
        dest_start (int): The starting index of the destination range
        source_start (int): The starting index of the source range
        length (int): The length of both ranges

    Returns:
        int: The new location after the mapping
    """
    if given >= source_start and given <= (source_start + length - 1):
        return (given - source_start) + dest_start
    else:
        return given


def main_day5_1(*args):
    data = get_input("day5_1")

    seeds = [int(s.group()) for s in re.finditer("\d+", data.split("\n")[0].split(":")[1])]
    map_sets = [[l.split(" ") for l in s.split('\n')[1:]] for s in data.split("\n\n")]
   
    min = float('inf')

    for seed in seeds:
        for map_set in map_sets:
            for op in map_set:
                result = almanac_op(seed, int(op[0]), int(op[1]), int(op[2]))
                if result != seed:
                    seed = result
                    break
            
        if seed < min: min = seed

    display("FINAL:", min, target="day5_1-output")

import sys
if not 'js' in sys.modules:  
    main_day5_1()