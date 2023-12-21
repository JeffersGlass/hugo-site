from abc import ABC, abstractmethod
from typing import List, Self, Optional

from enums import State, Pulse, Level, pulse_list

class Module(ABC):
    def __init__(self, destinations: Optional[List[Self]] = None):
        self._destinations = destinations

    def __repr__(self) -> str:
        return f"({self.__class__} destinations={','.join(self._destinations) if self._destinations else "\'\'"})"

    @abstractmethod
    def receive_pulse(p: Pulse):
        ...

class FlipFlop(Module):
    def __init__(self, destinations = None):
        self.state = State.OFF
        super().__init__(destinations)

    def receive_pulse(self, p: Pulse):
        ...

class Conjunction(Module):
    def __init__(self, destinations = None):
        self._destinations = destinations
        if self.destinations: 
            self.last_pulse = [Level.LO] * len(self._destinations)
        else:
            self.last_pulse = []
        super().__init__(destinations)

    @property
    def destinations(self):
        return self._destinations
    
    @destinations.setter
    def destinations(self, value):
        self._destinations = value
        self.last_pulse = [Level.LO] * len(self._destinations)

    def receive_pulse(p: Pulse):
        ...

class Broadcaster(Module):
    def receive_pulse(self, p: Pulse):
        for d in self._destinations:
            pulse_list.append(Pulse(to=d, level=p.level))