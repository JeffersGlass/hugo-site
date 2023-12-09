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

from itertools import pairwise
import re
import sys
from typing import Iterable

def get_next_number(l: Iterable[int]):
    if all(n == 0 for n in l): return 0

    diff_sequence = [a[1] - a[0] for a in pairwise(l)]
    diff_sequence.append(get_next_number(diff_sequence))
    result = l[-1] + diff_sequence[-1] 

    return result


def main_day9_1(*args):
    data = [[int(n.group()) for n in re.finditer(r"-?\d+", line)] for line in get_input("day9_1").split("\n")]
    
    result = sum(get_next_number(d) for d in data)

    display(result, target="day9_1-output")

if 'js' not in sys.modules:
    main_day9_1()