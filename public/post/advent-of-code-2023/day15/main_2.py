try:
    from pyscript import document
    from utils import get_input
except ImportError:
    def get_input(*args):
        with open("input.txt") as f:
            return f.read()
        
    def display(*args, **kwargs):
        if 'target' in kwargs:
            kwargs.pop('target')
        print(*args, **kwargs)
                

from dataclasses import dataclass
import re
import sys

def hash(s: str) -> int:
    value = 0
    for char in s:
        value += ord(char)
        value *= 17
        value %= 256
    return value

@dataclass
class Lens:
    label: str
    focal_length: str

    def __eq__(self, other):
        return self.label == other or (hasattr(other, "label") and self.label == other.label)

def main_day15_2(*args):
    data = get_input("day15_2")

    boxes = [[] for _ in range(256)]
    for command in data.split(','):
        print(f"Processing {command}")
        m = re.match(r"(?P<label>[a-zA-Z]+)(?P<inst>[-]|=)(?P<num>\d)?", command)
        label, inst = m.group("label"), m.group("inst")
        box = boxes[hash(label)]
        print(f"{label=} {inst=}")
        if inst == "-":
            if label in box: box.remove(label)
        elif inst == "=":
            focal_length = m.group("num")
            if label in box:
                location = box.index(label)
                box[location] = Lens(label=label, focal_length=focal_length)
            else:
                box.append(Lens(label=label, focal_length=focal_length))
        else:
            raise ValueError(f"Inst must be '-' or '=', not {inst}")

    for i, b in enumerate(boxes):
        if boxes:
            pass# print(f"{i}\t{b}")

    total = 0
    for i, b in enumerate(boxes):
        for l, lens in enumerate(b):
            total += (i + 1) * (l + 1) * (int(lens.focal_length))

    display(total, target="day15_2-output")

if not 'js' in sys.modules:
    main_day15_2()
