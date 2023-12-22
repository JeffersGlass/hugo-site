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

from itertools import count
from math import prod
from operator import attrgetter
import re
import sys
from typing import Iterable, Mapping    

from pulse import pulse_list, Pulse, Level
from module import Broadcaster, FlipFlop, Conjunction, Dummy, Module, Counter

def push_button_2(modules: Mapping[str, Module]):
    #button = Broadcaster([modules['broadcaster']])
    pulse_list.append(Pulse(_from='button', to='broadcaster', level=Level.LO))
    
    while(pulse_list):
        p: Pulse = pulse_list.popleft()
        modules[p.to].receive_pulse(p)


def hash_state(modules: Mapping[str, Module]) -> str:
    flops: Iterable[FlipFlop] = sorted((m for m in modules.values() if type(m) == FlipFlop), key=attrgetter('label'))
    return ''.join(f.label + ('H' if f.state == Level.HI else 'L') for f in flops)

def load_modules(data: Iterable[str]) -> dict[str, Module]:
    modules: dict[str, Module] = {}
    pattern = r"(?P<name>((?P<flag>[%&])(?P<label>[a-z]+))|broadcaster) -> (?P<destinations>[a-z ,]+)"
    # Build network
    for line in data:
        m = re.match(pattern, line)
        # Handle case with dummy 'output' destination
        if 'output' in m.group("destinations"):
            modules['output'] = Broadcaster(label="output", destinations=[])

        if m.group("flag") == "%":
            modules[m.group("label")] = FlipFlop(label=m.group("label"))
        elif m.group("flag") == "&":
            modules[m.group("label")] = Conjunction(label=m.group("label"))
        elif m.group("name") == "broadcaster":
            modules['broadcaster'] = Broadcaster(label="broadcaster")
        else:
            raise ValueError(f"Flag must be % or & or name must be 'broadcaster'; line was {line}")
    
    # Wire up modules
    for line in data:
        m = re.match(pattern, line)
        dests = [d.strip() for d in m.group("destinations").split(",")]
        if (label:= m.group("label")): modules[label].destinations = dests
        elif (name:= m.group("name")) == 'broadcaster': modules['broadcaster'].destinations = dests
        else: raise ValueError(f"Line was not a valid label or 'broadcaster': {line}")
         
        #Set up conjunction module inputs
        for d in dests:
            name = m.group("label") or 'broadcaster'
            if not d in modules: modules[d] = Counter(label=name)
            if type(modules[d]) == Conjunction: modules[d].last_pulse[name] = Level.LO
        
    return modules

def main_day20_2(*args):
    data = get_input("day20_2").split("\n")

    modules = load_modules(data)
    
    for i in count():
        push_button_2(modules)
        if not i % 10_000: print(i)
        if modules['rx'].count == 1:
            break 
        modules['rx'].count = 0
        
    print(f"{i=}") 

    result = None
    display(result, target="day20_2-output")

if not 'js' in sys.modules and __name__ == "__main__":
    main_day20_2()
