import sys
from rich import print as rprint
from rich.text import Text

from map import Map

def solve_12_1(data: list[str]):
    map = Map(data)

    start = [cell for cell in map.cells.values() if cell.label == "S"][0]
    end = [cell for cell in map.cells.values() if cell.label == "E"][0]

    paths_to_investigate = [[start]]
    paths_to_finish = []
    dead_ends = set()

    while paths_to_investigate:
        #print(len(paths_to_investigate))
        current_path = paths_to_investigate.pop()
        
        current_cell = current_path[-1]

        if current_cell == end:
            paths_to_finish.append(current_path)
            return

        new_neighbors = [n for n in current_cell.neighbors if
            n.value <= current_cell.value + 1 and
            n != end and 
            n not in current_path]

        if not new_neighbors:
            dead_ends.add(current_cell)
            return

        for n in new_neighbors:
            paths_to_investigate.append(current_path + [n])
        
        print_map(map, paths_to_investigate[-1])
        input()

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
    with open('inputtest.txt', 'r') as fp:
        data = fp.read().split('\n')

    print(solve_12_1(data))