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

from dataclasses import dataclass      
import operator
import re
import sys
from typing import Iterable

@dataclass
class Part:
    x: int
    m: int
    a: int
    s: int
    status: str = "InProgress"
    rule: str = "in"

    pattern = r"(?P<attribute>[xmas])(?P<op>[<>])(?P<num>\d+)"

    def test_rule(self, rule: str) -> bool:
        m = re.match(self.pattern, rule)

        if m.group("op") == "<": op = operator.lt
        elif m.group("op") == ">": op = operator.gt
        else: raise ValueError(f"Op must be < or > not {m.group('op')}")

        return op(getattr(self, m.group("attribute")), int(m.group("num")))
    
    def apply_flow(self, flow: Iterable[str]):
        #print(f"{flow} to part {self}")
        for rule in flow:
            if rule == "A":
                self.status = "A"
                return
            if rule == "R":
                self.status = "R"
                return
            
            if not any(char in rule for char in ("<", ">")):
                #print(f"Jumping to new rule {rule}")
                self.rule = rule
                return
            
            prep, new_rule = rule.split(":")
            if self.test_rule(prep):
                self.rule = new_rule
                if self.rule == "A":
                    self.status = "A"
                    return
                if self.rule == "R":
                    self.status = "R"
                    return
                
                #print(f"Updated rule to {self.rule}")
                return
        
        raise BufferError(f"Should have found a way out of flow {flow}")
        


def main_day19_1(*args):
    raw_flows, raw_parts = get_input("day19_1").split("\n\n")

    part_pattern = r"\{x=(?P<x>\d+),m=(?P<m>\d+),a=(?P<a>\d+),s=(?P<s>\d+)\}"
    parts = []
    for line in raw_parts.split('\n'):
        m = re.match(part_pattern, line)
        parts.append(Part(x=int(m.group("x")), m=int(m.group("m")), a=int(m.group("a")), s=int(m.group("s"))))

    flow_pattern = r"(?P<name>[a-z]+)\{(?P<rest>.+)\}"
    flows = {}
    for line in raw_flows.split("\n"):
        m = re.match(flow_pattern, line)
        flows[m.group("name")] = m.group("rest").split(",")

    for part in parts:
        while part.status not in ("A", "R"):
            #print(f"Applying '{part.rule}'", end = "")
            part.apply_flow(flows[part.rule])
        print(f"Part has status {part.status}")

    result = sum(sum([p.x, p.m, p.a, p.s]) for p in parts if p.status == "A")
    display(result, target="day19_1-output")

if not 'js' in sys.modules:
    main_day19_1()
