import string
import sys
from typing import Collection

charValue = {s: index + 1 for index, s in enumerate(string.ascii_lowercase)} |\
            {s: index + 27 for index, s in enumerate(string.ascii_uppercase)}
        
def scoreBy3(data):
    sum = 0
    for index, a in enumerate(data[::3]):
        b = data[index*3 + 1]
        c = data[index*3 + 2]
        common = (set(a) & set(b) & set(c))
        
        assert len(common) == 1
        common = common.pop()

        score = charValue[common]
        sum += score
    return sum

if 'pyodide' in sys.modules:
    def main_day3_2():
        data = get_input('day3_2').split('\n')
        display(f"{scoreBy3(data)= }",
            target="day3_2-output",
            append=False)

elif __name__ == "__main__":
    with open("input.txt", "r") as fp:
        data = fp.read()
    result = scoreBy3(data.split('\n'))
    print(f"{result= }")

    