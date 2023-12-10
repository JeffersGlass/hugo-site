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

from collections import defaultdict
import sys
from typing import List

import rich

def r(char: str):
    table = str.maketrans("|-JLF7", "│─┘└┌┐")
    return char.translate(table)

def replace_char(s, index, char):
    return s[:index] + char + s[index+1:]

def print_pipes_10_2(data, current, seen):
    for l, line in enumerate(data):
        for c, char in enumerate(line):
            if (l, c) == current: rich.print(f"[red]{r(char)}[/red]", end="")
            elif (l, c) in seen: rich.print((f"[green]{r(char)}[/green]"), end="")
            elif char == '.' : rich.print(f"[gray]{r(char)}[/gray]", end="")
            else: rich.print(f"[white]{r(char)}[/white]", end="")
        print("")

def count_inner_cells(data, loop):
    count = 0
    for l, line in enumerate(data):
        is_inside = False
        crossing_start = ""
        for c, char in enumerate(line):
            if (l, c) in loop:
                if char == "|": is_inside = not is_inside
                elif char in ("L", "F"): crossing_start = char
                elif char in ("7", "J") and crossing_start != "":
                    if char == "7" and crossing_start == "L": is_inside = not is_inside
                    elif char == "J" and crossing_start == "F": is_inside = not is_inside
                    crossing_start = ""
                if is_inside: color = "white"
                else: color = "white"
                rich.print(f"[{color}]{r(char)}[/{color}]", end = "")
            else:
                if is_inside: 
                    count += 1
                    rich.print(f"[white on green]{char}[/white on green]", end = "")
                else:
                    rich.print(f"[red]{char}[/red]", end = "")
        print("")
                

    return count


def main_day10_2(*args):
    data: List[str] = get_input("day10_2").split('\n')

    _map_data = {(line_num, char_num): char for line_num, line in enumerate(data) for char_num, char in enumerate(line)}
    map_data = defaultdict(lambda: None, _map_data)

    start_line, _start_line_data = [(index, line)for index, line in enumerate(data) if 'S' in line][0]
    start_char = _start_line_data.index('S')
    #print_pipes(data, [], [])

    north_entry = ('N', (1,0))
    east_entry = ('E', (0, -1))
    south_entry = ('S', (-1, 0))
    west_entry = ('W', (0, 1))

    instructions = {
        '|': {
            'N': north_entry,
            'S': south_entry
        },
        '-': {
            'E': east_entry,
            'W': west_entry
        },
        'L': {
            'N' : west_entry,
            'E' : south_entry
        },
        'J': {
            'N' : east_entry,
            'W' : south_entry
        },
        '7': {
            'S' : east_entry,
            'W' : north_entry,
        },
        'F': {
            'S' : west_entry,
            'E' : north_entry
        }
    }

    # Find starting direction:
    adjacent_dirs = [('W', (start_line, start_char + 1)) if map_data[(start_line, start_char + 1)] in ('-', 'J', '7') else "",
                     ('E', (start_line, start_char - 1)) if map_data[(start_line, start_char - 1)] in ('-', 'L', 'F') else "", 
                     ('N', (start_line + 1, start_char)) if map_data[(start_line + 1, start_char)] in ('|', 'L', 'J') else "", 
                     ('S', (start_line - 1, start_char)) if map_data[(start_line - 1, start_char)] in ('|', '7', 'F') else ""]

    entry_dir, position = [a for a in adjacent_dirs if a][0]
    
    count = 1
    loop = [(start_line, start_char), position]
    
    while (current_space:= map_data[position]) != 'S':
        count += 1
        entry_dir, position_delta = instructions[current_space][entry_dir]
        position = (position[0] + position_delta[0], position[1] + position_delta[1])
        loop.append(position)
        #print_pipes(data, position, seen)

    print(adjacent_dirs)
    starting_directions = tuple(a[0] for a in adjacent_dirs if a)
    print(starting_directions)
    if starting_directions == ('W', 'E'): data[start_line] = replace_char(data[start_line], start_char, "-")
    elif starting_directions == ('N', 'S'): data[start_line] = replace_char(data[start_line], start_char, "|")
    elif starting_directions == ('W', 'N'): data[start_line] = replace_char(data[start_line], start_char, "F")
    elif starting_directions == ('W', 'S'): data[start_line] = replace_char(data[start_line], start_char, "L")
    elif starting_directions == ('E', 'N'): data[start_line] = replace_char(data[start_line], start_char, "7")
    elif starting_directions == ('E', 'S'): data[start_line] = replace_char(data[start_line], start_char, "J")
    

    result = count_inner_cells(data, loop)

    display(result, target="day10_2-output")

if not 'js' in sys.modules:
    main_day10_2()
    #print(r("7"))
    #data = [".|L-7.F-J|."]
    #loop = ((0,1), (0,2), (0,3), (0,4), (0,6), (0,7), (0,8), (0,9))
    #count_inner_cells(data, loop)
