import math
import sys
from typing import Sequence

from monkey import Monkey



def run_one_monkey_11_2(monkey_list: Sequence[Monkey], monkey_index, lcm):
    monkey = monkey_list[monkey_index]

    while monkey.items:
        currentItem = monkey.items.popleft()
        currentItem = int(monkey.operation(currentItem)) % lcm
        if monkey.test(currentItem):
            monkey_list[monkey.true_dest].items.append(currentItem)
        else:
            monkey_list[monkey.false_dest].items.append(currentItem)
        monkey.throw_count += 1

def run_one_round_11_2(monkey_list, lcm):
    for i in range(len(monkey_list)):
        run_one_monkey_11_2(monkey_list, i, lcm)

def solve_11_2(data):
    monkeys = [Monkey.from_text(text)for text in data]

    MONKEY_LCM = math.prod([m.test_num for m in monkeys])

    for i in range(10_000):
        if i == 20 or not i % 1000:
            for m in monkeys:
                print(f"{i} {m.throw_count}")
        run_one_round_11_2(monkeys, MONKEY_LCM)

    most_active = sorted(monkeys, key=lambda m: m.throw_count)
    return most_active[-1].throw_count * most_active[-2].throw_count

if 'pyodide' in sys.modules:
    pass
else:
    with open('input.txt', 'r') as fp:
        data = fp.read().split("\n\n")

    print(solve_11_2(data))
    
    
    