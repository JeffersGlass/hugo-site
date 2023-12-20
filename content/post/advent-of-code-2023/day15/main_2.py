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
                
import sys

def main_day15_2(*args):
    data = get_input("day15_2")

    result = None
    display(result, target="day15_2-output")

if not 'js' in sys.modules:
    main_day15_2()
