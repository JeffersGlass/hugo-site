from collections import deque
import re
from typing import Callable, Sequence


class Monkey():
    def __init__(
        self,
        label: int,
        items: Sequence[int],
        operation: Callable[[int], int],
        test: Callable[[int], bool],
        test_num: int,
        true_dest: int,
        false_dest: int
    ):
        self.label: int = label
        self.items = deque(items)
        self.operation: Callable[[int], int] = operation
        self.test: Callable[[int], bool] = test
        self.test_num: int = test_num
        self.true_dest: int = true_dest
        self.false_dest: int = false_dest

        self.throw_count = 0

    def __repr__(self):
        return f"""Monkey(label={self.label}, \
items={self.items}, \
operation={self.operation}, \
test={self.test}, \
true_dest={self.true_dest}, \
false_dest={self.false_dest}), \
throw_count={self.throw_count}"""

    @classmethod
    def from_text(cls, text:str):
        lines: list[str] = text.split('\n')
        label: int = int(re.match(r'Monkey (?P<label>\d+)',lines[0]).group('label'))
        starting: list[int] = [int(d) for d in re.findall(r'(\d+)', lines[1])]

        operation = lines[2].removeprefix("  Operation: ").replace("new", "old").replace("=", ":")
        operation = eval(f"lambda {operation}")

        test_number = int(re.search(r'(\d+)', lines[3]).group())
        test = lambda x: x % test_number == 0

        to_dest = int(re.search(r'(\d+)', lines[4]).group())
        false_dest = int(re.search(r'(\d+)', lines[5]).group())

        return cls(label, starting, operation, test, test_number, to_dest, false_dest)
