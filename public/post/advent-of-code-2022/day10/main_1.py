import sys

if 'pyodide' in sys.modules:
    import js
    import os
    js.console.log(os.listdir('.'))

from typing import Iterable

from computer import Computer
from parser_10_1 import Parser_10_1


def solve_10_1(data):
    comp = Computer(instructions=iter(data), parser=Parser_10_1())
    signal_strength = 0

    for breakpoint in (20 + i * 40 for i in range(6)):
        comp.run_until_clock(breakpoint)
        #print(f"Current instruction is {comp._current_instruction} with {comp._current_instruction._ellapsed_ticks} ellapsed ticks at index {comp._instruction_index}")
        x_register = comp.reg_x.get()
        #print(f"{x_register=} ")
        signal_value = breakpoint * comp.reg_x.get()
        #print(f"At {breakpoint}, signal is {signal_value}")
        signal_strength += signal_value
        #print(f"Running total {signal_strength= }\n")

    return(signal_strength)

if 'pyodide' in sys.modules:
    def main_day10_1():
        data = get_input('day10_1').split("\n")
        display(f"{solve_10_1(data)=}",
            target="day10_1-output",
            append=False)
else:
    with open('input.txt', 'r') as fp:
        data = fp.read().split('\n')

    print(solve_10_1(data))