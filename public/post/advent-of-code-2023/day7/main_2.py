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

def score_lines_7_2(lines: Iterable[str]):
    """Take in a list of input sorted by rank, and return
    the score required by the pizzle

    Args:
        lines (Iterable[str]): A sorted Iterable of input lines

    Returns:
        _type_: _description_
    """
    return sum(int(line.split(" ")[1]) * (index+1) for index, line in enumerate(lines))

def sort_lines_7_2(lines: Iterable[str]):
    return sorted(lines, key = rank_7_2)

def rank_7_2(line):
    hand = line.split(" ")[0]
    if hand == "JJJJJ": return int("F11111", base=16)

    counts = Counter(hand)
    vals = [list(s) for s in sorted(counts.items(), key=itemgetter(1), reverse=True)]

    # Move count of jokers to the next-most-common card
    if vals[0][0] == 'J': vals[1][1] += vals[0][1]
    else: vals[0][1] += counts["J"]

    # Find the count that corresponds to jokers, and remove it
    j_items = [i for i in vals if i[0] == "J"]
    if j_items:
        vals.remove(j_items[0])
    
    vals = tuple(v[1] for v in vals)


    if vals == (5,): rank = "F" # 5 of a kind
    elif vals == (4,1): rank = "E" # 4 of a kind
    elif vals == (3,2): rank = "D" # Full House
    elif vals == (3,1,1): rank = "C" # Three of a kind
    elif vals == (2,2,1): rank = "B" # Two Pair
    elif vals == (2,1,1,1): rank = "A"
    else:rank = "9"
    
    new_card = rank + remap_card_names_7_2(hand)
    return int(new_card, base=16)

def remap_card_names_7_2(hand):
    trans = str.maketrans("AKQJT", "FED1B")
    return hand.translate(trans)

def main_day7_2(*args):
    data = get_input("day7_2").split("\n")

    data = sort_lines_7_2(data)
    for line in data:
        print(line)
    result = score_lines_7_2(data)

    display(result, target="day7_2-output")

try:
    import js
except ImportError:
    main_day7_2()