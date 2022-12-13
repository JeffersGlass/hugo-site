from instruction import Instruction

class Noop(Instruction):
    def tick(self) -> bool:
        self._ellapsed_ticks += 1
        return True #Only 1 tick

    def at_complete(self) -> None:
        self.computer.advance_instruction()