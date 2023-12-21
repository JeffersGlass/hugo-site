from abc import ABC, abstractmethod
from typing import List, Self

from enums import State, Pulse, Level

class Module(ABC):
    def __init__(self, destinations: List[Self]):
        self.destinations = destinations

    @abstractmethod
    def receive_pulse(p: Pulse):
        ...

class FlipFlop(Module):
    def __init__(self, destinations):
        self.state = State.OFF
        super().__init__(destinations)

class Conjunction(Module):
    def __init__(self, destinations):
        self.last_pulse = [Level.LO] * len(destinations)
        super().__init__(destinations)

class Broadcaster(Module):
    def receive_pulse(self, p: Pulse):
        for d in self.destinations:
            pulse_list.append(Pulse(to=d, level=p.level))