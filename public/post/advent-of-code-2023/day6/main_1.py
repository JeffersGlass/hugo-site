try:
    from pyscript import document
    from utils import get_input
except ImportError:
    def get_input(*args):
        with open("input_test.txt") as f:
            return f.read()
        
    def display(*args, **kwargs):
        if 'target' in kwargs:
            kwargs.pop('target')
        print(*args, **kwargs)

import re

def main_day6_1(*args):
    data = get_input("day6_1").split("\n")
    races = zip(
        (int(d.group()) for d in re.finditer("\d+", data[0])), # times
        (int(d.group()) for d in re.finditer("\d+", data[1]))  # distances
        )

    prod = 1
    for race in races:
        count = 0
        total_time, distance_goal = race
        for hold_time in range(total_time):
            if (total_time - hold_time) * hold_time > distance_goal: count +=1 
        prod *= count

    display(prod, target="day6_1-output")

try:
    import js
except ImportError:
    main_day6_1()
