import sys

from map import Map

def get_valid_neighbors(cell, dead_ends, end):
    return [n for n in cell.neighbors if n not in dead_ends and n != end]
   

def iterate_path_one_step(map, current_path, dead_ends, end_cell, paths_to_finish, paths_to_investigate):
    current_cell = current_path[-1]

    if current_cell == end_cell:
        paths_to_finish.append(current_path)
        return

    new_neighbors = get_valid_neighbors(current_cell, dead_ends, end_cell)

    if not new_neighbors:
        dead_ends.add(current_cell)
        return

    for n in new_neighbors:
        paths_to_investigate.append(current_path + [n])

def solve_12_1(data: list[str]):
    map = Map(data)

    start = [cell for cell in map.cells.values() if cell.name == "S"][0]
    end = [cell for cell in map.cells.values() if cell.name == "E"][0]

    paths_to_investigate = [[start]]
    paths_to_finish = []
    dead_ends = set()

    while dead_ends != map.cells:
        current_path = paths_to_investigate.pop()
        #print(current_path)
        iterate_path_one_step(map, current_path, dead_ends, end, paths_to_finish, paths_to_investigate)
        #input()


if 'pyodide' in sys.modules:
    pass
else:
    with open('inputtest.txt', 'r') as fp:
        data = fp.read().split('\n')

    print(solve_12_1(data))