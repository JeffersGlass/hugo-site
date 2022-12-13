from computer import Computer
from instruction import Instruction
from register import Register

class Addition(Instruction):
    def __init__(self, duration: int, computer: Computer, register: Register, addend: int):
        super().__init__(duration, computer)
        self.register: Register = register
        self.addend: int = addend

    def tick(self) -> bool:
        self._ellapsed_ticks += 1
        return self._ellapsed_ticks == 2

    def at_complete(self) -> None:
        self.register.set(self.register.get() + self.addend)
        self.computer.advance_instruction()