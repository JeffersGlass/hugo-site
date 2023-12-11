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

from itertools import combinations
import sys

def main_day11_2(*args):
    data = get_input("day11_2").split("\n")

    expanding_row_indices = [i for i, line in enumerate(data) if all(char == '.' for char in line)]
    expanding_col_indices = [i for i in range(len(data)) if all(line[i] == '.' for line in data)]
    stars =  [(line_index, char_index) for line_index, line in enumerate(data) for char_index, char in enumerate(line) if char == '#']

    total = 0
    for s1, s2, in combinations(stars, 2):
        manhattan_dist = abs(s2[0] - s1[0]) + abs(s2[1] - s1[1])
        
        # expanding rows; stars are in row order, so s2[0] >= s1[0]
        row_total = len([r for r in expanding_row_indices if s1[0] < r < s2[0]])

        # expanding columns, not necessarily ordered
        if s2[1] == s1[1]: 
            col_total = 0
        elif s2[1] > s1[1]:
            col_total = len([c for c in expanding_col_indices if s1[1] < c < s2[1]])
        else: # s2[1] < s1[1] 
            col_total = len([c for c in expanding_col_indices if s2[1] < c < s1[1]])

        total += manhattan_dist + row_total + col_total
    
    result = total
    display(result, target="day11_2-output")

if not 'js' in sys.modules:
    main_day11_2()