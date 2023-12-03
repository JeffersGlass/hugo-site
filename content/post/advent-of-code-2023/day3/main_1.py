try:
    from pyscript import document
    from utils import get_input
except ImportError:
    def get_input(*args):
        with open("input.txt") as f:
            return f.read()
        
    def display(*args, **kwargs):
        if 'target' in kwargs:
            dict.pop('target')
        print(*args, **kwargs)

from dataclasses import dataclass
from collections import namedtuple
import re
from typing import List

position = namedtuple('position', ['line', 'char'])

@dataclass
class Number:
    value: int
    line: int
    start: int
    end: int
    
def main_day3_1(*args):
    data = get_input("day3_1").split("\n")

    symbols = set()
    part_numbers: List[Number] = []

    symbol_pattern = re.compile("[^0123456789.]")
    number_pattern = re.compile("(\d+)")

    for line_index, line in enumerate(data):
        for s in re.finditer(symbol_pattern, line):
            symbols.add((line_index, s.start()))
        for n in re.finditer(number_pattern, line):
            part_numbers.append(Number(
                    value=int(n.group()),
                    line = line_index,
                    start = n.start(),
                    end = n.end()))
    
    sum = 0
    for number in part_numbers:
        if (number.line, number.start-1) in symbols or \
        (number.line, number.end) in symbols:
            sum += number.value
            continue

        for index in range(number.start-1, number.end+1):
            if (number.line-1, index) in symbols or\
            (number.line+1, index) in symbols:
                sum += number.value
                continue
    display(sum, target="day3_1-output")

# Only runs if not running in the browser
if __name__ == "__main__":
    try:
        import js
    except ImportError:     
        main_day3_1()