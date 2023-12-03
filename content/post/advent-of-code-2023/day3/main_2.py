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
from typing import List, Dict

position = namedtuple('position', ['line', 'char'])

@dataclass
class Gear:
    value: int = 0
    seen_once: bool = False 

@dataclass
class Number:
    value: int
    line: int
    start: int
    end: int

def processGear(g: Gear, part_number: int):
    """_summary_

    Args:
        g (Gear): The gear currently being processed
        part_number (int): The part number being processed

    Returns: The value to be added to the running sum, if any
    """
    if g.seen_once:
        g.value *= part_number.value
        g.seen_once = False # Seen twice
        return g.value
    else:
        if g.value == 0: 
            g.value = part_number.value
            g.seen_once = True

        return 0

    
    
def main_day3_2(*args):
    data = get_input("day3_2").split("\n")

    gears: Dict[position: Gear] = {}
    part_numbers: List[Number] = []

    gear_pattern = re.compile("[*]")
    number_pattern = re.compile("(\d+)")

    for line_index, line in enumerate(data):
        for s in re.finditer(gear_pattern, line):
            gears[position(line=line_index, char=s.start())] = Gear()
        for n in re.finditer(number_pattern, line):
            part_numbers.append(Number(
                    value=int(n.group()),
                    line = line_index,
                    start = n.start(),
                    end = n.end()))
    
    sum = 0

    for number in part_numbers:
        for pos in [(number.line, number.start-1), # left of number
                    (number.line, number.end), # right of number
                    *((number.line-1, index) for index in range(number.start-1, number.end+1)), # above number
                    *((number.line+1, index) for index in range(number.start-1, number.end+1))  # below number
                    ]:
            if pos in gears:
                sum += processGear(gears[pos], part_number=number)
        continue
    
    display(sum, target="day3_2-output")


# Only runs if not running in the browser
if __name__ == "__main__":
    try:
        import js
    except ImportError:     
        main_day3_2()