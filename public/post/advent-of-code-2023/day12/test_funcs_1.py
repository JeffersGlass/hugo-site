from main_1 import match, gen_runs_of_springs, min_length_of_sequence_set, count_valid_options

def test_match():
    assert match("####", "####") == True
    assert match("####", "????") == True
    assert match("####", "....") == False
    assert match("####", ".#..") == False
    assert match("####", "#?#?") == True
    assert match("....", "####") == False
    assert match("....", "????") == True
    assert match("....", ".?.?") == True
    assert match("..#.", "####") == False

def test_gen_runs_of_springs():
    assert gen_runs_of_springs(1, 4) == ["#...", ".#..", "..#.", "...#"]
    assert gen_runs_of_springs(3, 7) == ['###....', '.###...', '..###..', '...###.', '....###']

def test_min_length_of_sequence_set():
    assert min_length_of_sequence_set([1]) == 1
    assert min_length_of_sequence_set([1, 1]) == 3
    assert min_length_of_sequence_set([1,2]) == 4
    assert min_length_of_sequence_set([2,1]) == 4
    assert min_length_of_sequence_set([1,1,1]) == 5
    assert min_length_of_sequence_set([5,1]) == 7

def test_count_valid_options():
    assert count_valid_options([1], '????') == 4
    assert count_valid_options([1], '?#??') == 1
    assert count_valid_options([1], '##??') == 0
    assert count_valid_options([1], '..#?') == 1
    assert count_valid_options([1], '....') == 0
    assert count_valid_options([1], '.#..') == 1

    assert count_valid_options([2], '.##.') == 1
    assert count_valid_options([2], '.#?.') == 1
    assert count_valid_options([2], '.??.') == 1
    assert count_valid_options([2], '.???') == 2
    assert count_valid_options([2], '.?#?') == 2

    assert count_valid_options([1,1], '#.#') == 1
    assert count_valid_options([1,1], '#.?') == 1
    assert count_valid_options([1,1], '?.?') == 1
    assert count_valid_options([1,1], '#.??') == 2
    assert count_valid_options([1,1], '??.??') == 4

    assert count_valid_options([1,2], '#.##') == 1
    assert count_valid_options([1,2], '?.??') == 1
    assert count_valid_options([1,2], '??.??') == 2

    assert count_valid_options([1,1,3], '??..###') == 0

def test_examples():
    assert count_valid_options([1,1,3], '???.###') == 1
    assert count_valid_options([1,1,3], '.??..??...?##.') == 4
    assert count_valid_options([1,3,1,6], '?#?#?#?#?#?#?#?') == 1
    assert count_valid_options([4,1,1], '????.#...#...') == 1
    assert count_valid_options([1,6,5], '????.######..#####.') == 4
    assert count_valid_options([3,2,1], '?###????????') == 10
    