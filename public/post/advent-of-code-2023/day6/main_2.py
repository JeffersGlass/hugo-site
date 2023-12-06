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

import re

def main_day6_2(*args):
    data = get_input("day6_2").split("\n")
    total_time = int(''.join(d.group() for d in re.finditer('\d', data[0])))
    distance_goal = int(''.join(d.group() for d in re.finditer('\d', data[1])))

    count = 0
    for hold_time in range(total_time):
        if (total_time - hold_time) * hold_time > distance_goal: count +=1 

    display(count, target="day6_2-output")

try:
    import js
except ImportError:
    main_day6_2()
