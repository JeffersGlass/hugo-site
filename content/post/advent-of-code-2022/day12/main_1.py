import sys
from functools import partial
from rich import print as rprint
from rich.text import Text

from map import Map, Cell

def solve_12_1(data: list[str]):
    map = Map(data)

    start = [cell for cell in map.cells.values() if cell.label == "S"][0]
    end = [cell for cell in map.cells.values() if cell.label == "E"][0]

    paths_to_investigate = [[start]]
    paths_to_finish = []
    dead_ends = set()

    it = 0

    while paths_to_investigate:
        it += 1
        if not it % 10_000:
            print_map(map, paths_to_investigate[-1])
            print(f"{len(paths_to_investigate)= } : {len(paths_to_finish)= } : High Value: {paths_to_investigate[-1][-1].label}")



        current_path = paths_to_investigate.pop()
        
        current_cell = current_path[-1]

        if current_cell.location == end.location:
            paths_to_finish.append(current_path)
            continue

        new_neighbors = [n for n in current_cell.neighbors if
            n.value <= current_cell.value + 1 and
            n not in current_path]

        if not new_neighbors:
            #dead_ends.add(current_cell)
            continue

        for n in new_neighbors:
            paths_to_investigate.append(current_path + [n])

        paths_to_investigate.sort(key = lambda path: ord(path[-1].label))
        
        #print_map(map, paths_to_investigate[-1])
        #print(f"{len(paths_to_investigate)= } : {len(paths_to_finish)= } ")
    
    return min(len(path) for path in paths_to_finish) - 1

def astar(destination: Cell, current: Cell):
    return -1 * ((destination.row  - current.row) ** 2 + (destination.column - current.column) ** 2)

def print_map(map: Map, path = None):
    for row in range(map.rows):
        for column in range(map.columns):
            char = Text(map.cells[(row, column)].label)
            if path and any([(row, column) == pathcell.location for pathcell in path]): char.stylize("red")
            else: char.stylize("green")
            rprint(char, end="")
        rprint("")

if 'pyodide' in sys.modules:
    pass
else:
    with open('input.txt', 'r') as fp:
        data = fp.read().split('\n')

    print(solve_12_1(data))