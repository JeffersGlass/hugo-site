import sys
from typing import Sequence

from monkey import Monkey

def run_one_monkey(monkey_list: Sequence[Monkey], monkey_index):
    monkey = monkey_list[monkey_index]

    while monkey.items:
        currentItem = monkey.items.popleft()
        currentItem = int(monkey.operation(currentItem) / 3)
        if monkey.test(currentItem):
            monkey_list[monkey.true_dest].items.append(currentItem)
        else:
            monkey_list[monkey.false_dest].items.append(currentItem)
        monkey.throw_count += 1

def run_one_round(monkey_list):
    for i in range(len(monkey_list)):
        run_one_monkey(monkey_list, i)

def solve_11_1(data):
    monkeys = [Monkey.from_text(text)for text in data]

    for m in monkeys:
        print(m)

    for _ in range(20):
        run_one_round(monkeys)

    most_active = sorted(monkeys, key=lambda m: m.throw_count)
    return most_active[-1].throw_count * most_active[-2].throw_count

if 'pyodide' in sys.modules:
    pass
else:
    with open('input.txt', 'r') as fp:
        data = fp.read().split("\n\n")

    print(solve_11_1(data))
    
    
    