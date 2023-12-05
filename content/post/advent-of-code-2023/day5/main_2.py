try:
    from pyscript import document
    from utils import get_input
except ImportError:
    def get_input(*args):
        with open("input.txt") as f:
            return f.read()
        
    def display(*args, **kwargs):
        if 'target' in kwargs:
            dict.pop('target')
        print(*args, **kwargs)

def main_day5(*args):
    data = get_input("day5")

    result = None
    display(result, target="day5-output")
