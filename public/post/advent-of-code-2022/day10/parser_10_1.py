from instructionparser import InstructionParser, InstructionParseException
from instruction import Instruction
from computer import Computer

from addition import Addition
from noop import Noop


class Parser_10_1():
    def parse(self, instruction: str, computer: Computer) -> Instruction:
        str_instruction = instruction.split()
        match str_instruction:
            case ["noop"]:
                return Noop(1, computer)
            case ["addx", value] :
                return Addition(duration=2, computer=computer, register = computer.reg_x, addend = int(value))
            case _:
                raise InstructionParseException(f"No instruction matching '{instruction}'")

if __name__ == "__main__":
    with open('inputtest_long.txt', 'r') as fp:
        data = fp.read().split('\n')
    
    p = Parser_10_1()
    computer = Computer(None)

    for line in data:
        print(p.parse(instruction=line, computer=computer))