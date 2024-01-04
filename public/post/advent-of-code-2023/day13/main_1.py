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
                
import sys
from typing import List

# Vertical Mirrors - index 0 is between first_line[0] and first_line[1]
def find_vertical_mirror(pattern: List[str]) -> int | None:
    pattern = pattern.split("\n")
    for seam_index in range(len(pattern[0])-1):
        good_seam = True # sentinel to allow shortcutting out of the loop
        for lower, upper in zip(range(seam_index, -1, -1), range(seam_index+1, len(pattern[0]))):
            if any(line[lower] != line[upper] for line in pattern):
                good_seam = False
                break
        if good_seam: return seam_index + 1 # Counted in original problem is one different from this index

def find_horizontal_mirror(pattern: List[str]) -> int | None:
    pattern = pattern.split("\n")
    for seam_index in range(len(pattern)-1):
        good_seam = True
        for lower, upper in zip(range(seam_index, -1, -1), range(seam_index+1, len(pattern))):
            if any(pattern[lower][i] != pattern[upper][i] for i in range(len(pattern[0]))):
                good_seam = False
                break
        if good_seam: return seam_index + 1



def main_day13_1(*args):
    patterns = get_input("day13_1").split("\n\n")

    total = 0
    for pattern in patterns:
        if mirror_index := find_vertical_mirror(pattern):
            total += mirror_index
        elif mirror_index := find_horizontal_mirror(pattern):
            total += 100 * mirror_index

    display(total, target="day13_1-output")

if not 'js' in sys.modules:
    main_day13_1()
