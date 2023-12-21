from pyvis.network import Network
import networkx as nx

import re 

from pulse import Level
from module import Broadcaster, FlipFlop, Conjunction, Dummy, Module, Counter

G = nx.DiGraph()

with open("input.txt", "r") as f:
    data = f.readlines()

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

def color_by_class(obj):
    t = type(obj)
    if t == Broadcaster: return 'red'
    elif t == FlipFlop: return 'blue'
    elif t == Conjunction: return 'green'
    elif t == Counter: return 'orange'
    else: return 'purple'

for label, m in modules.items():
    G.add_node(label, color=color_by_class(m))

G.add_nodes_from(modules.keys(), )
for label, m in modules.items():
    if m.destinations:
        for d in m.destinations:
            G.add_edge(label, d,)

# populates the nodes and edges data structures
nt = Network('1200px', '1200px', directed=True)
nt.from_nx(G)
nt.show('nx.html', notebook=False)

