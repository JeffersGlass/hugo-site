from typing import NamedTuple
import re
import sys
from typing import NewType

# The 'yard' is the collection of all the stacks of crates
yardType = NewType("yardType", dict[str:list])

class Instruction(NamedTuple):
    quantity: int
    from_stack: str
    to_stack: str

def solutionFromInput(data: str) -> str:
    data = data.split("\n")
    stacks, instructions = parseInput(data)
    for ins in instructions:
        stacks = operateOn(stacks, ins)
    return topCrates(stacks)

def parseInput(data: list[str]) -> tuple[yardType, list[Instruction]]:
    firstBlankLine = data.index("")
    cratePositions = data[:firstBlankLine]
    cratePositions.reverse() #ordered bottom to top
    instructionLines = data[firstBlankLine+1:]

    # Create crate data struction
    crateNameLine = cratePositions[0] #get crate labels from line
    crates = {name: [] for name in crateNameLine.split()} #create dicts per line
    for line in cratePositions[1:]:
        for index, crateName in enumerate(line[1::4]):
            if crateName != " ":
                crates[str(crateNameLine[index*4 + 1])].append(crateName) #Add crate to list
    
    # Parse instructions
    instructions = []
    for ins in instructionLines:
        match = re.match(r'move (?P<num>\d+) from (?P<from_stack>\d+) to (?P<to_stack>\d+)', ins)
        num, from_stack, to_stack = match.group('num'), match.group('from_stack'), match.group('to_stack')

        instructions.append(Instruction(
                quantity = int(match.group('num')),
                from_stack = match.group('from_stack'),
                to_stack = match.group('to_stack')
            ))
    
    return (crates, instructions)

def operateOn(crates: yardType, ins: Instruction) -> yardType:
    to_move = crates[ins.from_stack][-ins.quantity:]
    crates[ins.from_stack] = crates[ins.from_stack][:-ins.quantity]
    crates[ins.to_stack].extend(to_move)
    return crates

def topCrates(crates: yardType):
    return ''.join([stack.pop() for stack in crates.values()])
    

if 'pyodide' in sys.modules:
    pass
else:
    with open("input.txt", "r") as fp:
        data = fp.read()
    print(solutionFromInput(data))