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

def print_pipes(data, current, seen):
    for l, line in enumerate(data):
        for c, char in enumerate(line):
            if (l, c) == current: rich.print(f"[red]{char}[/red]", end="")
            elif (l, c) in seen: rich.print((f"[green]{char}[/green]"), end="")
            elif char == '.' : rich.print(f"[gray]{char}[/gray]", end="")
            else: rich.print(f"[white]{char}[/white]", end="")
        print("")

def main_day10_1(*args):
    data: List[str] = get_input("day10_1").split('\n')

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
    seen = [(start_line, start_char), position]
    
    while (current_space:= map_data[position]) != 'S':
        count += 1
        entry_dir, position_delta = instructions[current_space][entry_dir]
        position = (position[0] + position_delta[0], position[1] + position_delta[1])
        seen.append(position)
        #print_pipes(data, position, seen)

    result = count / 2
    display(result, target="day10_1-output")

if not 'js' in sys.modules:
    main_day10_1()
