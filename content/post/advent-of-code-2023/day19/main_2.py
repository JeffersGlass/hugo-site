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
from math import prod
import re
import sys
from typing import Iterable, Self

@dataclass
class PartRange:
    x_min: int
    x_max: int
    m_min: int
    m_max: int
    a_min: int
    a_max: int
    s_min: int
    s_max: int
    status: str = "InProgress"
    rule: str = "in"

    pattern = r"(?P<attribute>[xmas])(?P<op>[<>])(?P<num>\d+)"

    @staticmethod
    def fromPartRange(other, x_min=None, x_max=None, m_min = None, m_max = None, a_min = None, a_max = None, s_min = None, s_max = None, rule=None):
        return PartRange(x_min=x_min or other.x_min, x_max=x_max or other.x_max,
                         m_min=m_min or other.m_min, m_max=m_max or other.m_max,
                         a_min=a_min or other.a_min, a_max=a_max or other.a_max,
                         s_min=s_min or other.s_min, s_max=s_max or other.s_max,
                         rule = rule or other.rule)

    def count(self):
        return prod([(self.x_max - self.x_min + 1),(self.m_max - self.m_min + 1),(self.a_max - self.a_min + 1),(self.s_max - self.s_min + 1)])
    
    def apply_flow(self, flow: str) -> Iterable[Self]:
        outgoing = []
        for rule in flow.split(","):
            if rule == "A": 
                self.status = "A"
                outgoing.append(self)
                return outgoing
            if rule == "R":
                self.status = "R"
                return outgoing
        
            if not any(char in rule for char in ("<", ">")):
                self.rule = rule
                outgoing.append(self)
                return outgoing
            
            prep, new_rule = rule.split(":")
            m = re.match(self.pattern, prep)

            attr = m.group("attribute")
            num = int(m.group("num"))

            if m.group("op") == "<":
                if int(getattr(self, attr+"_min")) <= num:
                    first_kwargs = {attr+ "_max": num-1}
                    outgoing.append(self.fromPartRange(self, rule=new_rule, **first_kwargs))
                    setattr(self, attr+"_min", num)
                    continue

            elif m.group("op") == ">":
                if int(getattr(self, attr+"_max")) >= num:
                    first_kwargs = {attr+ "_min": num+1}
                    outgoing.append(self.fromPartRange(self, rule=new_rule, **first_kwargs))
                    setattr(self, attr+"_max", num)
                    continue

            raise ValueError(f"Rule {rule} did not match anything")                
      

def main_day19_2(*args):
    raw_flows, raw_parts = get_input("day19_2").split("\n\n")

    flow_pattern = r"(?P<name>[a-z]+)\{(?P<rest>.+)\}"
    flows = {}
    for line in raw_flows.split("\n"):
        m = re.match(flow_pattern, line)
        flows[m.group("name")] = m.group("rest")

    ranges = [PartRange(x_min=1, x_max=4000,m_min=1, m_max=4000,a_min=1, a_max=4000,s_min=1, s_max=4000)]

    accepted = []
    while ranges:
        r = ranges.pop()
        if r.status == "A" or r.rule == "A":
            accepted.append(r)
        elif r.status == "R" or r.rule == "R":
            pass
        else:
            ranges.extend(r.apply_flow(flows[r.rule]))

    print(sum(r.count() for r in accepted))

    result = None
    display(result, target="day19_2-output")

if not 'js' in sys.modules:
    main_day19_2()
