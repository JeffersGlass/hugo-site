from dataclasses import dataclass
from functools import partial

import js
from js import anime, Object
from pyodide.ffi import to_js, create_proxy

from main_1 import parseInput, yardType, Instruction

def j(obj):
    return to_js(obj, dict_converter=Object.fromEntries)

with open("input.txt", "r") as fp:
    data = fp.read().split('\n')
yard, instructions = parseInput(data)

@dataclass
class Crate():
    label:str
    element:object

    def __str__(self):
        return self.label

@dataclass
class Stack():
    crates: list
    x: int

overall = js.document.getElementById("day5_2-viz")
overall.style.margin = "50px 50px 50px 50px"
overall.style.position = "relative"
div = js.document.createElement('div')
overall.appendChild(div)

divHeight = 800
divWidth = 600

div.style.height = f"{divHeight}px"
div.style.width = f"{divWidth}px"
div.style.backgroundColor = "#eee"

floorY = divHeight - 100

floor = js.document.createElement('div')
floor.id = "floor"
floor.style.backgroundColor = "#777"
floor.style.position = "absolute"
floor.style.height = "10px"
floor.style.width = f"{divWidth + 100}px"
floor.style.bottom = f"{divHeight-floorY-10}px"
floor.style.left = "-50px"
overall.appendChild(floor)

textOutput = js.document.createElement("div")
textOutput.id = "day5_2_text_output"
overall.parentNode.insertBefore(textOutput, overall.nextSibling)

crateSize = 25

def indexToBottom(index):
    return divHeight - floorY + (crateSize+5) * index

def indexToTop(index):
    return divHeight - floorY + crateSize + (crateSize + 5) * index

def makeDisplay(yard):
    for index, stack in enumerate(yard):
        newStackList = []
        leftEdge = index * (crateSize * 2) + 25

        stackLabel = js.document.createElement('div')
        stackLabel.style.width = f"{crateSize}px"
        stackLabel.style.height = f"{crateSize}px"
        stackLabel.style.position = "absolute"
        stackLabel.style.left = f"{leftEdge}px"
        stackLabel.style.top = f"{floorY + 15}px"
        stackLabel.style.textAlign = "center"
        label = js.document.createElement("span")
        label.innerText = stack
        stackLabel.appendChild(label)
        div.appendChild(stackLabel)

        for stackLevel, crate in enumerate(yard[stack]):
            bottom = indexToBottom(stackLevel)
            container = js.document.createElement('div')
            container.style.width = f"{crateSize}px"
            container.style.height = f"{crateSize}px"
            container.style.backgroundColor = "Aquamarine"
            container.style.border = "2px solid #2c2e34"
            container.style.position = "absolute"#div.style.padding = "2rem 2rem 2rem 2rem"
            container.style.bottom = f"{bottom}px"
            container.style.left = f"{leftEdge}px"
            container.style.textAlign = "center"

            label = js.document.createElement("span")
            label.innerText = str(crate)
            container.appendChild(label)

            newStackList.append(Crate(crate, container))
            div.appendChild(container)
        yard[stack] = Stack(crates= newStackList, x = leftEdge)

makeDisplay(yard)

myTimeline = anime.timeline(j({
    "duration": 500,
    "easing": "easeInOutSine",
    "autoplay": False
}))

js.startAnimation = myTimeline.play
js.stopAnimation = myTimeline.pause
js.myTimeline = myTimeline

progressElement = js.document.getElementById("seekbar")

def updateSeekbar(*args):
    progressElement.value = myTimeline.progress


def displayOnMove(from_stack, to_stack, quantity, instructionCount, instructionIndex, *args):
    display(f"Instruction {instructionIndex}: Move {quantity} crate{'s' if quantity > 1 else ''} from stack {from_stack} to stack {to_stack}. {instructionCount+1} of {quantity} complete", target="day5_2_text_output", append=False)

def doFinalOutput(yard, *args):
    solution = ""
    for stack in yard:
        if len(yard[stack].crates):
            topCrate = yard[stack].crates[-1]
            topCrate.element.style.backgroundColor = "green"
            solution += topCrate.label
    display(f"SOLUTION: {solution}", target="day5_2_text_output", append=False)

def moveOneCrate(yard: yardType, from_stack: str, to_stack: str, quantity: int, timeline, instructionCount, instructionIndex, final):
    js.console.log("moveOneCrate")
    crate = yard[from_stack].crates.pop()
    yard[to_stack].crates.append(crate)
    newBottom = indexToBottom(yard[to_stack].crates.index(crate))
    timeline.add(j({
        "targets": crate.element,
        "keyframes": [
            j({"bottom": f"{divHeight - 20 - crateSize}px"}),
            j({"left": yard[to_stack].x}),
            j({"bottom": f"{newBottom}px"})
        ],
        "begin": partial(displayOnMove, from_stack, to_stack, quantity, instructionCount, instructionIndex),
        "update": updateSeekbar,
        "complete": partial(doFinalOutput, yard) if final else (lambda _: None)
    }))
    
    

def operateOn(yard: yardType, ins: Instruction, instructionIndex: int, final:bool) -> yard:
    for instructionCount in range(ins.quantity):
        moveOneCrate(yard, ins.from_stack, ins.to_stack, ins.quantity, myTimeline, instructionCount, instructionIndex, final = final and instructionCount == ins.quantity - 1)

def doAllInstructions(instructions):
    for instructionIndex, ins in enumerate(instructions):
        operateOn(yard, ins, instructionIndex, final = True if instructionIndex == len(instructions) - 1 else False)

doAllInstructions(instructions)

js.console.log(js.window)