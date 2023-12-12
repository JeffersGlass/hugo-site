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
                
import sys
from typing import Iterable, List

def match(value: str, pattern: str) -> bool:
    """Whether the given value is valid given the (start) of
    the pattern. 

    Consider inlining this.

    Args:
        value (str): The value to be checked
        pattern (str): The pattern to match

    Returns:
        bool: Whether the value is valid given the (initial) part of the pattern
    """
    return all(pattern[i] == '?' or value[i] == pattern[i] for i in range(len(value)))

def gen_runs_of_springs(num_springs: int, max_len: int) -> List[str]:
    """All the possible ways of slotting a group of num_springs "#" chars
    into a sequnce of length max_len

    Args:
        num_springs (int): The number broken springs in a group
        max_len (int): The length of sequences to generatre

    Returns:
        List[str]: The generated sequences of strings
    """
    return ['.'*i + '#' * num_springs + '.'*(max_len-num_springs-i) for i in range(max_len-num_springs+1)]

def min_length_of_sequence_set(sequences: Iterable[int]) -> int:
    """The minimum length you can squeeze a sequence of groupings of springs into,
    with a single '.' between them

    Args:
        sequences (Iterable[int]): The sequnces of springs

    Returns:
        int: The minimum space
    """
    if len(sequences) == 1: return len(sequences)
    return sum(sequences) + len(sequences) - 1

def count_valid_options(sequences: Iterable[int], pattern, prefix = ''):
    print(f"Counting valid options for {sequences} against {pattern}")
    if len(sequences) == 1:
        g = [s for s in gen_runs_of_springs(sequences[0], len(pattern)) if match(s, pattern)]
        print([prefix + new for new in g])
        return len(g)
    else:
        count = 0
        min_space_for_first_group = sequences[0] + 1
        max_space_for_first_group = len(pattern) - min_length_of_sequence_set(sequences[1:])
        # TODO there is an error in here, not accounting for needing a '.' between groups if the first
        # group ends in a "#""
        for length_for_first_group in range(min_space_for_first_group, max_space_for_first_group+1):
            for possibilty in gen_runs_of_springs(sequences[0], length_for_first_group):
                if match(possibilty, pattern):
                    count += count_valid_options(sequences[1:], pattern[length_for_first_group:])
        return count
        

def main_day12_1(*args):
    data = get_input("day12_1").split("\n")

    result = None
    display(result, target="day12_1-output")

if not 'js' in sys.modules:
    pass
    #main_day12_1()

