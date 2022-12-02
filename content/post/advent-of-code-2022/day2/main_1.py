import sys

def translateLine(s):
    return s.translate(str.maketrans({"A": "X", "B": "Y", "C": "Z"}))

def scoreFromStrategy(theirs, mine):
    selectedShapePoints = {"X": 1, "Y": 2, "Z": 3}
    points = selectedShapePoints[mine]
    if theirs == mine: #draw
        points += 3
    elif  ((theirs, mine) == ("X", "Y") or
        (theirs, mine) == ("Y", "Z") or
        (theirs, mine) == ("Z", "X")): #win
        points += 6
    return points

def scoreFromInput(data):
    return sum(scoreFromStrategy(*translateLine(line).split(" ")) for line in data)

if 'pyodide' in sys.modules:
    def main_day2_1():
        data = get_input('day2_1').split('\n')
        display(f"{scoreFromInput(data)= }",
            target="day2_1-output",
            append=False)

else:
    if __name__ == "__main__":
        with open('input.txt', 'r') as fp:
            data = fp.read().split('\n')
            print(f"{scoreFromInput(data)= }")