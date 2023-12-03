try:
    from pyscript import document
    from utils import get_input
except ImportError:
    pass

import re
    
def main_day2_1(*args):
    data = get_input("day2_2").split("\n")
    color_pattern = re.compile("(?P<quantity>\d+) (?P<color>(?:red)|(?:green)|(?:blue))")
    
    sum = 0
    for line in data:
        max_red, max_green, max_blue = 0, 0, 0

        colors = re.finditer(color_pattern, line)
        for c in colors:
            color, quant = c.group('color'), int(c.group('quantity'))
            if color == 'red' and quant > max_red: max_red = quant
            if color == 'green' and quant > max_green: max_green = quant
            if color == 'blue' and quant > max_blue: max_blue = quant     
        power = max_red * max_green * max_blue
        sum += power
    
    display(sum)

# Only runs if not running in the browser
if __name__ == "__main__":
    def get_input(*args):
        with open("input.txt") as f:
            return f.read()
        
    def display(*args, **kwargs):
        if 'target' in kwargs:
            dict.pop('target')
        print(*args, **kwargs)
        
    main_day2_1()