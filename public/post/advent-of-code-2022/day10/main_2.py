import sys
from typing import Iterable

from computer import Computer
from screen import Screen
from parser_10_1 import Parser_10_1

if 'pyodide' in sys.modules:
    pass
else:
    with open('input.txt', 'r') as fp:
        data = fp.read().split('\n')

    screen = Screen()
    comp = Computer(instructions=iter(data), parser=Parser_10_1())

    while True:
        input_from_computer = comp.reg_x.get()
        screen.tick(input_from_computer)
        should_continue = comp.run_single_step()
        if not should_continue:
            break

    print(screen)