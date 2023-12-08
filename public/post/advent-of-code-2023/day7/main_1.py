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

from collections import Counter
from operator import itemgetter
import re
from typing import Iterable

pat = re.compile("\d+")

def score_lines_7_1(lines: Iterable[str]):
    """Take in a list of input sorted by rank, and return
    the score required by the pizzle

    Args:
        lines (Iterable[str]): A sorted Iterable of input lines

    Returns:
        _type_: _description_
    """
    return sum(int(line.split(" ")[1]) * (index+1) for index, line in enumerate(lines))

def sort_lines_7_1(lines: Iterable[str]):
    return sorted(lines, key = rank_7_1)

def rank_7_1(line):
    print(f"Ranking {line}", end = "\t")
    hand = line.split(" ")[0]
    counts = Counter(hand)
    vals = tuple(sorted((counts.values()), reverse=True))
    if vals == (5,): rank = "F" # 5 of a kind
    elif vals == (4,1): rank = "E" # 4 of a kind
    elif vals == (3,2): rank = "D" # Full House
    elif vals == (3,1,1): rank = "C" # Three of a kind
    elif vals == (2,2,1): rank = "B" # Two Pair
    elif vals == (2,1,1,1): rank = "A"
    else:rank = "9"
    print(f"{rank=}", end="\t")
    new_card = rank + remap_card_names_7_1(hand)
    print(f"{new_card=}")
    return int(rank+remap_card_names_7_1(hand), base=16)

def remap_card_names_7_1(hand):
    trans = str.maketrans("AKQJT", "FEDCB")
    return hand.translate(trans)

def main_day7_1(*args):
    data = get_input("day7_1").split("\n")

    result = score_lines_7_1(sort_lines_7_1(data))

    display(result, target="day7_1-output")

try:
    import js
except ImportError:
    main_day7_1()