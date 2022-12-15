from typing import Iterable

from instructionparser import InstructionParser
from register import Register

class Computer():
    def __init__(self, instructions: Iterable[str], parser: InstructionParser = None):
        self.instructions = instructions
        self.parser = parser

        self.reg_x = Register(1)

        self.clock_counter = 1
        self._instruction_index = -1
        self.advance_instruction()
        

    def run(self) -> None:
        print("Computer running")

        while self._current_instruction is not None:
            self.next()

    def run_single_step(self) -> bool:
        """ Returns True if successfully completed a step, false if halted"""

        if self._current_instruction is not None:
            self.next()
            return True
        else:
            return False

    def run_until_clock(self, cycles) -> None:
        print(f"Computer running until clock is {cycles}")

        while self.clock_counter < cycles and self._current_instruction is not None:
            self.next()

    def next(self) -> None:
        if self._current_instruction == None:
            self._current_instruction = self.parser.parse(next(self.instructions))
        
        instruction_complete = self._current_instruction.tick()
        if (instruction_complete):
            self._current_instruction.at_complete()
            
        self.clock_counter += 1
    
    def advance_instruction(self) -> None:
        try:
            self._current_instruction = self.parser.parse(next(self.instructions), self)
            self._instruction_index += 1
            #print(f"Instruction advanced to {self._current_instruction}")
        except StopIteration:
            self._current_instruction = None
        
