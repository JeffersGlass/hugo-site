import sys
from typing import Iterable

from computer import Computer
from parser_10_1 import Parser_10_1

if 'pyodide' in sys.modules:
    pass
else:
    with open('input.txt', 'r') as fp:
        data = fp.read().split('\n')

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

    print(signal_strength)