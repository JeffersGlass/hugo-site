from collections import deque
import sys

def findIndexAllDifferent_5_2(input_stream, n):
    window = deque(maxlen=n)
    for index, token in enumerate(input_stream):
        window.append(token)
        print(window)
        if index + 1 >= n and len(set(window)) >= n:
            #print(f"{len(set(window))} {set(window)}")
            return index + 1


if 'pyodide' in sys.modules:
    pass
else:
    with open("input.txt", "r") as fp:
        data = fp.read().strip('\n')
    print(findIndexAllDifferent_5_2(data, 14))
    