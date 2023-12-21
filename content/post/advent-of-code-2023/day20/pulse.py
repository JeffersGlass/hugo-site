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
    _from: str
    to: str
    level: Level

class PulseList(deque):
    def __init__(self, *args, **kwargs):
        self.count = 0
        super().__init__(*args, **kwargs)

    def append(self,p:Pulse):
        self.count += 1
        print(f"Sending {p.level} Pulse from {p._from} to {p.to}")
        super().append(p)

pulse_list = PulseList()