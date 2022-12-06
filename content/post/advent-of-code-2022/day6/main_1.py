from collections import deque
import sys

def findIndexAllDifferent(input_stream, n):
    window = deque(maxlen=n)
    for index, token in enumerate(input_stream):
        window.append(token)
        if index + 1 >= n and len(set(window)) >= n:
            return index + 1
    return -1

if 'pyodide' in sys.modules:
    def main_day6_1():
        data = get_input('day6_1')
        display(f"{findIndexAllDifferent(data, 4)= }",
            target="day6_1-output",
            append=False)
else:
    with open("input.txt", "r") as fp:
        data = fp.read().strip('\n')
    print(findIndexAllDifferent(data, 4))
    