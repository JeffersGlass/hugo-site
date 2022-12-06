from collections import deque
import sys

def findIndexAllDifferent_6_2(input_stream, n):
    window = deque(maxlen=n)
    for index, token in enumerate(input_stream):
        window.append(token)
        if index + 1 >= n and len(set(window)) >= n:
            return index + 1
    return -1

if 'pyodide' in sys.modules:
    def main_day6_2():
        data = get_input('day6_2')
        display(f"{findIndexAllDifferent_6_2(data, 14)= }",
            target="day6_2-output",
            append=False)
else:
    with open("input.txt", "r") as fp:
        data = fp.read().strip('\n')
    print(findIndexAllDifferent_6_2(data, 14))