from itertools import repeat
from typing import Iterable
from sys import stdout

from pyscript import display, HTML

from rich import get_console
from rich.segment import Segment
from rich.console import NewLine
from rich.text import Text
import rich.jupyter

# Patch the rich library to enable output

c = get_console()
c.is_jupyter = lambda: True

def get_rich_printer(target):
    def display_pyscript(segments: Iterable[Segment], text: str) -> None:
        """Allow output of raw HTML within pyscript/pyodide"""
        html = rich.jupyter._render_segments(segments)
        display(HTML(html), target=target, append=True)
    rich.jupyter.display = display_pyscript
    return get_console().print

#Solution code

def viz_day8_2():
    prepare_day8_2_element()
    js.document.getElementById("day8_2-viz").innerHTML = ""
    data = get_input('day8_2').split('\n')
    display(f"{solution_viz8_2(data)=}",
        target="day8_2-output",
        append=False)
    post_day8_2_element()

def prepare_day8_2_element():
    viz_div = js.document.getElementById("day8_2-viz")
    viz_div.classList.add("overflow-x-auto", "overflow-y-auto", "w-full", "whitespace-nowrap")

def post_day8_2_element():
    from pyodide.ffi import to_js

    viz_div = js.document.getElementById("day8_2-viz")
    for pretag in viz_div.getElementsByTagName('pre'):
        pretag.style.whiteSpace = "nowrap"
        pretag.style.display = "inline-block"

def solution_viz8_2(data: list[str]):
    max_trees_visible = 0
    high_score_location = None
    visible_from_high_score = set()

    for house_row_index, treehouse_row in enumerate(data):
        for house_col_index, treehouse_height in enumerate(treehouse_row):
        
            visible_trees = set()
            score = 1

            #Row left to right
            row_to_right = data[house_row_index][house_col_index+1:]

            visbile_from_func = find_visible_in_line_viz8_2(row_to_right, max_height=int(treehouse_height))
            visible_trees |= {(house_row_index, line_index + house_col_index + 1) for line_index in visbile_from_func}
            score *= len(visbile_from_func)
            
            #Rows right to left
            row_to_left = list(reversed(data[house_row_index][:house_col_index]))
            visbile_from_func = find_visible_in_line_viz8_2(row_to_left, max_height=int(treehouse_height))
            visible_trees |= {(house_row_index, house_col_index - 1 - line_index) for line_index in visbile_from_func}
            score *= len(visbile_from_func)

            #Columns Top to Bottom:
            column_down = [row[house_col_index] for row in data[house_row_index+1:]]
            visbile_from_func = find_visible_in_line_viz8_2(column_down, max_height=int(treehouse_height))
            visible_trees |= {(house_row_index + line_index + 1, house_col_index) for line_index in visbile_from_func}
            score *= len(visbile_from_func)
            
            #Columns bottom to top:
            column_up = list(reversed([row[house_col_index] for row in data[:house_row_index]]))
            visbile_from_func = find_visible_in_line_viz8_2(column_up, max_height=int(treehouse_height))
            visible_trees |= {(house_row_index - line_index - 1, house_col_index) for line_index in visbile_from_func}
            score *= len(visbile_from_func)

            if score > max_trees_visible:
                max_trees_visible = score
                high_score_location = (house_row_index, house_col_index)
                visible_from_high_score = visible_trees
    
    printVisibleTrees_viz_8_2(data, visible_from_high_score, special=high_score_location)

    return max_trees_visible


def printVisibleTrees_viz_8_2(data: list[str], visbile_trees: set[tuple[int, int]], special = None):
    row_strings = []
    for row_index, row in enumerate(data):
        line_elements = []
        for column_index, char in enumerate(row):
            if (row_index, column_index) == special:
                line_elements.append(f"[bright_white on dark_violet]{char}[/]")
            elif (row_index, column_index) in visbile_trees:
                line_elements.append(f"[bright_white on dark_green]{char}[/]")
            else:
                line_elements.append(f"[aquamarine3]{char}[/]")
        row_strings.append(''.join(line_elements))
    
    for r in row_strings:
        get_rich_printer("day8_2-viz")(r)

def find_visible_in_line_viz8_2(line: str, max_height = 9) -> int:
    #print(f"Visible in line {list(line)} from height {max_height}; ", end = "")
    visible_trees = set()

    if not line:
        #print("Nothing here, score 0")
        return visible_trees

    for line_index, tree in enumerate(line):
        if int(tree) >= max_height:
            #print(f"Score: {line_index+1}")
            return range(0, line_index+1)
    else:
        #print(f"Max length, score {len(line)}")
        return range(0, len(line))