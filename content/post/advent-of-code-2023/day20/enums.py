from enum import Enum, auto
from dataclasses import dataclass
from collections import deque

class Level(Enum):
    LO = auto()
    HI = auto()

class State(Enum):
    ON = auto()
    OFF = auto()

@dataclass
class Pulse:
    to: str
    level: Level.LO | Level.HI

pulse_list = deque()