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
from typing import List, Collection, Optional


import rich

def printPattern(pattern: str,
                 hl_cols: Optional[Collection] = None,
                 hl_rows: Optional[Collection] = None,
                 hl_locations: Optional[Collection] = None,
                 hl_color = 'green'):
    pattern = pattern.split("\n")
    for line_index, line in enumerate(pattern):
        for char_index, char in enumerate(line):
            if hl_locations and (line_index, char_index) in hl_locations:
                rich.print(f"[yellow]{char}[/yellow]", end = "")
            elif (hl_cols and char_index in hl_cols) or (hl_rows and line_index in hl_rows):
                rich.print(f"[{hl_color}]{char}[/{hl_color}]", end = "")
            else:
                print(char, end = "")
        print("")
                

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
    print("Looking for smudged vertical mirror")
    pattern = pattern.split("\n")
    for seam_index in range(len(pattern[0])-1):
        smudge_count = 0
        good_seam = True # sentinel to allow shortcutting out of the loop
        for lower, upper in zip(range(seam_index, -1, -1), range(seam_index+1, len(pattern[0]))):
            print(f"Comparing columns {lower=} and {upper=}")
            #printPattern('\n'.join(pattern), hl_cols=(lower, upper))
            #print("")
            smudge_count += [line[lower] == line[upper] for line in pattern].count(False)
            #if smudge_count > 1: #If count is to high, exist immediately
                #good_seam = False
                #break
        print(f"{smudge_count=}\n")
        if good_seam and smudge_count == 1:
            print("FOUND THE SMUDGE")
            return seam_index + 1 # Counted in original problem is one different from this index

def find_smudged_horizontal_mirror(pattern: List[str]) -> int | None:
    pattern = pattern.split("\n")
    for seam_index in range(len(pattern)-1):
        smudge_count = 0
        good_seam = True # sentinel to allow shortcutting out of the loop
        for lower, upper in zip(range(seam_index, -1, -1), range(seam_index+1, len(pattern))):
            print(f"Comparing rows {lower=} and {upper=}")
            #printPattern('\n'.join(pattern), hl_rows=(lower, upper))
            smudge_count += [pattern[lower][i] == pattern[upper][i] for i in range(len(pattern[0]))].count(False)
            #if smudge_count > 1:
            #    good_seam = False
            #    break
        print(f"{smudge_count=}\n")
        if good_seam and smudge_count == 1: return seam_index + 1 # Counted in original problem is one different from this index



def main_day13_2(*args):
    patterns = get_input("day13_2").split("\n\n")
    patterns = [patterns[i] for i in (14, )] #(14, 16, 54, 58, 72, 85)

    total = 0
    for index, pattern in enumerate(patterns): 
        print(f"Examining pattern {index}")
        if smudge_index := find_smudged_vertical_mirror(pattern):
            if smudge_index != find_vertical_mirror(pattern):
                total += smudge_index
        elif smudge_index := find_smudged_horizontal_mirror(pattern):
            if smudge_index != find_horizontal_mirror(pattern):
                total += 100 * smudge_index
        else:
            print(f"No smudge found in pattern {index} (line {sum(len(pattern.split('\n')) for pattern in patterns[:index])})")

    display(total, target="day13_1-output")

if not 'js' in sys.modules:
    main_day13_2()
