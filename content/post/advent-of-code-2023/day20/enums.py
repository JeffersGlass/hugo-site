from enum import Enum, auto
from dataclasses import dataclass
from collections import deque
from typing import Any

class Level(Enum):
    LO = auto()
    HI = auto()

class State(Enum):
    ON = auto()
    OFF = auto()

@dataclass
class Pulse:
    to: str
    level: Level

class PulseList(deque):
    def __init__(self, *args, **kwargs):
        self.count = 0
        super().__init__(*args, **kwargs)

    def append(self,x:Any):
        self.count += 1
        super().append(x)

pulse_list = PulseList()