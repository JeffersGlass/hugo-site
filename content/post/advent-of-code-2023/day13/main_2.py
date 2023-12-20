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

# Vertical Mirrors - index 0 is between first_line[0] and first_line[1]
def find_smudged_vertical_mirror(pattern: List[str]) -> int | None:
    pattern = pattern.split("\n")
    for seam_index in range(len(pattern[0])-1):
        smudge_count = 0
        good_seam = True # sentinel to allow shortcutting out of the loop
        for lower, upper in zip(range(seam_index, -1, -1), range(seam_index+1, len(pattern[0]))):
            smudge_count += [line[lower] == line[upper] for line in pattern].count(False)
            if smudge_count > 1: #If count is to high, exist immediately
                good_seam = False
                break
        if good_seam and smudge_count == 1: return seam_index + 1 # Counted in original problem is one different from this index

def find_smudged_horizontal_mirror(pattern: List[str]) -> int | None:
    pattern = pattern.split("\n")
    for seam_index in range(len(pattern)-1):
        smudge_count = 0
        good_seam = True # sentinel to allow shortcutting out of the loop
        for lower, upper in zip(range(seam_index, -1, -1), range(seam_index+1, len(pattern))):
            smudge_count += [pattern[lower][i] == pattern[upper][i] for i in range(len(pattern[0]))].count(False)
            if smudge_count > 1:
                good_seam = False
                break
        if good_seam and smudge_count == 1: return seam_index + 1 # Counted in original problem is one different from this index



def main_day13_2(*args):
    patterns = get_input("day13_2").split("\n\n")

    total = 0
    for index, pattern in enumerate(patterns): 
        if smudge_index := find_smudged_vertical_mirror(pattern):
            if smudge_index != find_vertical_mirror(pattern):
                total += smudge_index
        elif smudge_index := find_smudged_horizontal_mirror(pattern):
            if smudge_index != find_horizontal_mirror(pattern):
                total += 100 * smudge_index
        else:
            print(f"No smudge found in pattern {index} (line {sum(len(pattern.split("\n")) for pattern in patterns[:index])})")

    display(total, target="day13_1-output")

if not 'js' in sys.modules:
    main_day13_2()
