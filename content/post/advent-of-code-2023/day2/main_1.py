try:
    from pyscript import document
    from utils import get_input
except ImportError:
    print("Getting local input")    
    def get_input(*args):
        with open("input.txt") as f:
            return f.read()
        
    def display(*args, **kwargs):
        if 'target' in kwargs:
            dict.pop('target')
        print(*args, **kwargs)

import re
    

def main_day2_1(*args):
    data = get_input("day2_1").split("\n")

    day_pattern = re.compile("Game (?P<day_number>\d+)")
    color_pattern = re.compile("(?P<quantity>\d+) (?P<color>(?:red)|(?:green)|(?:blue))")
    
    sum = 0
    for line in data:
        id_value = int(re.match(day_pattern, line).group("day_number"))
        pulls = line.split(";")
        valid_line = True
        for p in pulls:
            if not valid_line: break
            colors = re.finditer(color_pattern, p)
            for c in colors:
                color, quant = c.group('color'), int(c.group('quantity'))
                if (color == 'red' and quant > 12) or (color == 'green' and quant > 13) or (color == 'blue' and quant > 14): 
                    valid_line = False
                    id_value = 0
                    break                    
        sum += id_value
    
    display(sum, target="day2_1-output")

# Only runs if not running in the browser
import sys
if not 'js' in sys.modules:
    main_day2_1()