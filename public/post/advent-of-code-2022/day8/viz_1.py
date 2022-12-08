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

# Solution code:
import js

def viz_day8_1():
    prepare_day8_1_element()
    js.document.getElementById("day8_1-viz").innerHTML = ""
    data = get_input('day8_1').split('\n')
    display(f"{solve_viz8_1(data)=}",
        target="day8_1-output",
        append=False)
    post_day8_1_element()


def prepare_day8_1_element():
    viz_div = js.document.getElementById("day8_1-viz")
    viz_div.classList.add("overflow-x-auto", "overflow-y-auto", "w-full", "whitespace-nowrap")


def post_day8_1_element():
    from pyodide.ffi import to_js

    viz_div = js.document.getElementById("day8_1-viz")
    for pretag in viz_div.getElementsByTagName('pre'):
        pretag.style.whiteSpace = "nowrap"
        pretag.style.display = "inline-block"


def solve_viz8_1(data: list[str]):
    # (rowIndex, columnIndex)
    visible_trees: set[tuple[int, int]] = set()

    #Rows left to right
    for row_index, row in enumerate(data):
        visible_trees |= {(row_index, line_index) for line_index in find_visible_in_line_viz(row)}
        pass

    #Rows right to left
    for row_index, row in enumerate([row[::-1] for row in data]):
        visible_trees |= {(row_index, len(row) - line_index - 1) for line_index in find_visible_in_line_viz(row)}
        pass

    #Columns Top to Bottom:
    for column_index in range(len(data[0])):
        column = [row[column_index] for row in data]
        visible_trees |= {(row_index, column_index) for row_index in find_visible_in_line_viz(column)}

    #Columns Bottom to Top:
    for column_index in range(len(data[0])):
        column = [row[column_index] for row in data][::-1]
        visible_trees |= {(len(column) - row_index - 1, column_index) for row_index in find_visible_in_line_viz(column)}
        
    printVisibleTrees_viz(data, visible_trees)

    return(len(visible_trees))

def printVisibleTrees_viz(data: list[str], visbile_trees: set[tuple[int, int]]):
    row_strings = []
    for row_index, row in enumerate(data):
        line_elements = []
        for column_index, char in enumerate(row):
            if (row_index, column_index) in visbile_trees:
                line_elements.append(f"[bright_white on dark_green]{char}[/]")
            else:
                line_elements.append(f"[aquamarine3]{char}[/]")
        row_strings.append(''.join(line_elements))
    
    for r in row_strings:
        get_rich_printer("day8_1-viz")(r)
        #rprint_8_1_viz(r)

def find_visible_in_line_viz(line: str) -> set[int]:
    max_height_seen = -1
    visible_in_line = set()

    for line_index, tree in enumerate(line):
        if int(tree) > max_height_seen:
            visible_in_line.add(line_index)
            max_height_seen = int(tree)
            if max_height_seen == 9: break

    return visible_in_line     