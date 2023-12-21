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
import sys

from enums import pulse_list, Pulse, Level
from module import Broadcaster, FlipFlop, Conjunction, Module

def main_day20_1(*args):
    data = get_input("day20_1").split("\n")

    modules: dict[str, Module] = {}
    pattern = r"(?P<name>((?P<flag>[%&])(?P<label>[a-z])+)|broadcaster) -> (?P<destinations>[a-z ,]+)"
    # Build network
    for line in data:
        m = re.match(pattern, line)
        if m.group("flag") == "%":
            modules[m.group("label")] = FlipFlop()
        elif m.group("flag") == "&":
            modules[m.group("label")] = Conjunction()
        elif m.group("name") == "broadcaster":
            modules['broadcaster'] = Broadcaster()
        else:
            raise ValueError(f"Flag must be % or & or name must be 'broadcaster'; line was {line}")
    
    # Wire up modules
    for line in data:
        m = re.match(pattern, line)
        dests = [d.strip() for d in m.group("destinations").split(",")]
        if (label:= m.group("label")): modules[label]._destinations = dests
        elif (name:= m.group("name")) == 'broadcaster': modules['broadcaster']._destinations = dests
        else: raise ValueError(f"Line was not a valid label or 'broadcaster': {line}")

    #button = Broadcaster([modules['broadcaster']])
    pulse_list.append(Pulse('broadcaster', Level.LO))
    
    while(pulse_list):
        p: Pulse = pulse_list.popleft()
        modules[p.to].receive_pulse(p)

    print(f"{pulse_list.count=}")

    result = None
    display(result, target="day20_1-output")

if not 'js' in sys.modules:
    main_day20_1()
