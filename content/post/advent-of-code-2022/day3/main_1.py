import string
import sys

charValue = {s: index + 1 for index, s in enumerate(string.ascii_lowercase)} |\
            {s: index + 27 for index, s in enumerate(string.ascii_uppercase)}

def prioritySum(data):
    sum = 0    
    for line in data:
        midpoint = int(len(line)/2)
        first = set(line[:midpoint])
        second = set(line[midpoint:])
        sum += charValue[(first & second).pop()]
    return sum

if 'pyodide' in sys.modules:
    def main_day3_1():
        data = get_input('day3_1').split('\n')
        display(f"{prioritySum(data)= }",
            target="day3_1-output",
            append=False)

elif __name__ == "__main__":
    with open("input.txt", "r") as fp:
        data = fp.read()
    result = prioritySum(data.split('\n'))
    print(f"{result= }")


    