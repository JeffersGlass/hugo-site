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
                
import sys

def main_day21_1(*args):
    data = get_input("day21_1").split("\n")

    empties = set((line_index, char_index) for line_index, line in enumerate(data) for char_index, char in enumerate(line) if char == "." or char == "S")
    steps = set([(line_index, char_index) for line_index, line in enumerate(data) for char_index, char in enumerate(line) if char == 'S'])
    width = len(data[0])
    height = len(data)
    
    for _ in range(64):
        new_steps = set()
        for step in steps:
            new_steps |= set([(step[0]+1, step[1]),
                             (step[0]-1, step[1]),
                             (step[0], step[1]+1), 
                             (step[0], step[1]-1)])
        steps = new_steps &empties  

    print(steps)

    result = len(steps)

    display(result, target="day21_1-output")

if not 'js' in sys.modules:
    main_day21_1()
