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

def get_previous_number(seq: Iterable[int]):
    if all(n == 0 for n in seq): return 0

    diff_sequence = [a[1] - a[0] for a in pairwise(seq)]
    diff_sequence.insert(0, get_previous_number(diff_sequence))
    result = seq[0] - diff_sequence[0] 

    return result


def main_day9_2(*args):
    data = [[int(n.group()) for n in re.finditer(r"-?\d+", line)] for line in get_input("day9_2").split("\n")]
    
    result = sum(get_previous_number(d) for d in data)

    display(result, target="day9_2-output")

if 'js' not in sys.modules:
    main_day9_2()