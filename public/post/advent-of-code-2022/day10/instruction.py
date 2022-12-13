from abc import ABC, abstractmethod
#from computer import Computer

class Instruction(ABC):
    def __init__(self, duration: int, computer):
        self.duration = duration
        self.computer = computer

        self._ellapsed_ticks = 0

    @abstractmethod
    def tick(self) -> bool:
        ...

    @abstractmethod
    def at_complete(self) -> None:
        ...

    