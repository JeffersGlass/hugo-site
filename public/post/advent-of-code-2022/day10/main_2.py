import sys
from typing import Iterable

from computer import Computer
from screen import Screen
from parser_10_1 import Parser_10_1

def solve_10_2(data):
    screen = Screen()
    comp = Computer(instructions=iter(data), parser=Parser_10_1())

    while True:
        input_from_computer = comp.reg_x.get()
        screen.tick(input_from_computer)
        should_continue = comp.run_single_step()
        if not should_continue:
            break

    return str(screen)

if 'pyodide' in sys.modules:
    def prepare_10_2():
        import js
        viz_div = js.document.getElementById("day10_2-viz")
        pre = js.document.createElement("pre")
        pre.id = "day10_1-pre"
        pre.classList.add("bg-gray-900", "text-gray-300")
        pre.style.lineHeight = '1.1'
        viz_div.appendChild(pre)

    def main_day10_2():
        data = get_input('day10_2').split("\n")
        prepare_10_2()
        display(f"{solve_10_2(data)}",
            target="day10_1-pre",
            append=False)
else:
    with open('input.txt', 'r') as fp:
        data = fp.read().split('\n')

    print(solve_10_2(data))
