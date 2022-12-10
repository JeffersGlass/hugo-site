from abc import ABC, abstractclassmethod

from instruction import Instruction

class InstructionParser(ABC):
    @abstractclassmethod
    def parse(instruction: str, computer) -> Instruction:
        ...

class InstructionParseException(Exception):
    ...