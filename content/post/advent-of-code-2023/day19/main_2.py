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
from math import prod
import re
import sys
from typing import Iterable, Self

@dataclass
class PartRange:
    x: tuple[int, int]
    m: tuple[int, int]
    a: tuple[int, int]
    s: tuple[int, int]
    status: str = "InProgress"
    rule: str = "in"

    pattern = r"(?P<attribute>[xmas])(?P<op>[<>])(?P<num>\d+)"

    @staticmethod
    def fromPartRange(other, x_min=None, x_max=None, m_min = None, m_max = None, a_min = None, a_max = None, s_min = None, s_max = None, rule=None):
        return PartRange(x=(x_min or other.x[0], x_max or other.x[1]),
                         m=(m_min or other.m[0], m_max or other.m[1]),
                         a=(a_min or other.a[0], a_max or other.a[1]),
                         s=(s_min or other.s[0], s_max or other.s[1]),
                         rule = rule or other.rule
        )

    def count(self):
        return prod(z[1] - z[0] for z in (self.x, self.m, self.a, self.s))
    
    def apply_flow(self, rule: str) -> Iterable[Self]:
        outgoing = []
        # TODO hmmmmmm
        if self.rule == "A": 
            self.status = "A"
            return
        if self.rule == "R":
            self.status = "R"
            return
        
        if not any(char in rule for char in ("<", ">")):
            #print(f"Jumping to new rule {rule}")
            self.rule = rule
            return
        
        
        prep, new_rule = rule.split(":")
        m = re.match(self.pattern, prep)

        if m.group("op") == "<":
            first_kwargs = {m.group("attribute")+ "_min": int(m.group("num"))}
            second_kwargs = {m.group("attribute")+ "_max": int(m.group("num"))}
            return [self.fromPartRange(self, rule=new_rule, **first_kwargs),
                    self.fromPartRange(self, rule=new_rule, **second_kwargs)]
                    
        elif m.group("op") == "<":
            kwargs = {m.group("attribute")+ "_max": int(m.group("num"))}
            return self.fromPartRange(self, rule=new_rule, **kwargs)
        else: raise ValueError(f"Op must be < or > not {m.group('op')}")

        
      

def main_day19_2(*args):
    raw_flows, raw_parts = get_input("day19_2").split("\n\n")

    flow_pattern = r"(?P<name>[a-z]+)\{(?P<rest>.+)\}"
    flows = {}
    for line in raw_flows.split("\n"):
        m = re.match(flow_pattern, line)
        flows[m.group("name")] = m.group("rest").split(",")

    ranges = [PartRange(x=(1,4000),m=(1,4000),a=(1,4000),s=(1,4000))]
    r = ranges[0].test_rule('s<1351:px')
    print(r)

    result = None
    display(result, target="day19_2-output")

if not 'js' in sys.modules:
    main_day19_2()
