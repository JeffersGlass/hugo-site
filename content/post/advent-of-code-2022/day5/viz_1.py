def viz_day5_1():
    from typing import NamedTuple
    from dataclasses import dataclass
    from functools import partial
    import re

    import js
    from js import anime, Object
    from pyodide.ffi import to_js, create_proxy
    from pyodide.ffi.wrappers import add_event_listener

    from typing import NewType

    # The 'yard' is the collection of all the stacks of crates
    yardType = NewType("yardType", dict[str:list])

    class Instruction(NamedTuple):
        quantity: int
        from_stack: str
        to_stack: str

    def j(obj):
        return to_js(obj, dict_converter=Object.fromEntries)

    data = get_input('day5_1').split('\n')        

    def parseInput(data: list[str]) -> tuple[yardType, list[Instruction]]:
        firstBlankLine = data.index("")
        cratePositions = data[:firstBlankLine]
        cratePositions.reverse() #ordered bottorstBlankLine = data.index("")
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

    overall = js.document.getElementById("day5_1-viz")
    overall.style.margin = "50px 50px 50px 50px"
    overall.style.position = "relative"
    div = js.document.createElement('div')
    overall.appendChild(div)

    divHeight = 800
    divWidth = 600

    startColor = "Aquamarine"
    endColor = "green"

    div.style.height = f"{divHeight}px"
    div.style.width = f"{divWidth}px"
    div.style.backgroundColor = "#eee"

    floorY = divHeight - 100

    floor = js.document.createElement('div')
    floor.id = "floor"
    floor.style.backgroundColor = "#777"
    floor.style.position = "absolute"
    floor.style.height = "10px"
    floor.style.width = f"{divWidth}px"
    floor.style.bottom = f"{divHeight-floorY-10}px"
    floor.style.left = "0px"
    overall.appendChild(floor)

    textOutput = js.document.createElement("div")
    textOutput.id = "day5_1_text_output"
    overall.parentNode.insertBefore(textOutput, overall.nextSibling)

    #<button onclick="startAnimation()">Play</button>
    #js.startAnimation = myTimeline.play
    playButton = js.document.createElement("button")
    playButton.innerText = "Play"
    playButton.style.padding = ".5rem 1rem .5rem 1rem"
    playButton.style.border = "2px solid #2c2e34"
    playButton.style.backgroundColor = "#bbf7d0"
    

    #<button onclick="stopAnimation()">Pause</button>
    #js.stopAnimation = myTimeline.pause
    pauseButton = js.document.createElement("button")
    pauseButton.innerText = "Pause"
    pauseButton.style.padding = ".5rem 1rem .5rem 1rem"
    pauseButton.style.border = "2px solid #2c2e34"
    pauseButton.style.backgroundColor = "#fef08a"

    #<input type="range" id="seekbar" min="0" max="100" value="0" oninput="myTimeline.pause();myTimeline.seek(myTimeline.duration * (this.value/100))" style="width: 100%"></progress>
    seekbar = js.document.createElement("input")
    seekbar.type = "range"
    seekbar.id = "seekbar"
    seekbar.min = "0"
    seekbar.max = "100"
    seekbar.value = "0"
    seekbar.style.width = "400px"

    controlHolder = js.document.createElement("div")
    controlHolder.id = "day5_2_controls"
    controlHolder.appendChild(playButton)
    controlHolder.appendChild(pauseButton)
    controlHolder.appendChild(seekbar)
    controlHolder.style.position = "absolute"
    controlHolder.style.bottom = "10px"
    controlHolder.style.left = "20px"
    controlHolder.style.width = "100%"
    div.appendChild(controlHolder)

    crateSize = 25

    def indexToBottom(index):
        return divHeight - floorY + (crateSize+5) * index

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
                container.style.backgroundColor = startColor
                container.style.width = f"{crateSize}px"
                container.style.border = "2px solid #2c2e34"
                container.style.position = "absolute"
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
        "autoplay": True
    }))

    def seekbar_input(evt):
        myTimeline.pause()
        myTimeline.seek(myTimeline.duration * (float(evt.srcElement.value)/100))

    add_event_listener(seekbar, 'input', seekbar_input)
    add_event_listener(playButton, 'click', lambda _: myTimeline.play())
    add_event_listener(pauseButton, 'click', lambda _: myTimeline.pause())

    progressElement = js.document.getElementById("seekbar")
    prevProgress = 0

    def updateSeekbar(yard, *args):
        nonlocal prevProgress
        progressElement.value = myTimeline.progress
        if myTimeline.progress == 100:
            for stack in yard:
                if len(yard[stack].crates):
                    topCrate = yard[stack].crates[-1]
                    topCrate.element.style.backgroundColor = endColor
        elif prevProgress == 100:
            for stack in yard:
                for crate in yard[stack].crates:
                    crate.element.style.backgroundColor = startColor

        prevProgress = myTimeline.progress


    def displayOnMove(from_stack, to_stack, quantity, instructionCount, instructionIndex, *args):
        display(f"Instruction {instructionIndex}: Move {quantity} crate{'s' if quantity > 1 else ''} from stack {from_stack} to stack {to_stack}. {instructionCount+1} of {quantity} complete", target="day5_1_text_output", append=False)

    def doFinalOutput(yard, *args):
        solution = ""
        for stack in yard:
            if len(yard[stack].crates):
                topCrate = yard[stack].crates[-1]
                topCrate.element.style.backgroundColor = "green"
                solution += topCrate.label
        display(f"SOLUTION: {solution}", target="day5_1_text_output", append=False)

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
            "update": partial(updateSeekbar, yard),
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