from abc import ABC, abstractmethod
from typing import List, Self, Optional

from pulse import State, Pulse, Level, pulse_list

class Module(ABC):
    def __init__(self, label, destinations: Optional[List[Self]] = None):
        self.label = label
        self.destinations = destinations

    def __repr__(self) -> str:
        return f"({self.__class__} label={self.label} destinations={','.join(self.destinations) if self.destinations else "\'\'"})"
    
    def send_to_all(self, level: Level):
        for d in self.destinations:
            pulse_list.append(Pulse(_from=self.label, to=d, level=level))

    @abstractmethod
    def receive_pulse(self, p: Pulse):
        ...

class FlipFlop(Module):
    def __init__(self, label, destinations = None):
        self.state = State.OFF
        super().__init__(label, destinations)

    def receive_pulse(self, p: Pulse):
        if p.level == Level.LO:
            if self.state == State.OFF:
                self.state = State.ON
                self.send_to_all(Level.HI)
            else:
                self.state = State.OFF
                self.send_to_all(Level.LO)

class Conjunction(Module):
    def __init__(self, label, destinations = None, inputs: List[str] = None):
        self._destinations = destinations
        if inputs is not None:
            self.last_pulse = {i: Level.LO for i in inputs}
        else: self.last_pulse = {}

        super().__init__(label, destinations)

    # TODO something in this is broken
    def receive_pulse(self, p: Pulse):
        print(f"{p}")
        self.last_pulse[p._from] == p.level
        print(f"{self} has levels {self.last_pulse}")
        if all(value == Level.HI for value in self.last_pulse.values()):
            self.send_to_all(Level.LO)
        else:
            self.send_to_all(Level.HI)

class Broadcaster(Module):
    def receive_pulse(self, p: Pulse):
        self.send_to_all(p.level)