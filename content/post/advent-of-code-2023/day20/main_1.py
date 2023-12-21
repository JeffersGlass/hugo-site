try:
    from pyscript import document
    from utils import get_input
except ImportError:
    def get_input(*args):
        with open("input_test.txt") as f:
            return f.read()
        
    def display(*args, **kwargs):
        if 'target' in kwargs:
            kwargs.pop('target')
        print(*args, **kwargs)
                
from abc import ABC, abstractmethod
from collections import deque
from dataclasses import dataclass
from enum import Enum, auto
import sys
from typing import List, Self

from enums import Level, State, pulse_list

def main_day20_1(*args):
    data = get_input("day20_1")

    result = None
    display(result, target="day20_1-output")

if not 'js' in sys.modules:
    main_day20_1()
