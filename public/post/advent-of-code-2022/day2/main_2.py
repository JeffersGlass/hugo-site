from itertools import cycle
import sys

def translateLine(s):
    return s.translate(str.maketrans({"A": "X", "B": "Y", "C": "Z"}))

def scoreFromStrategy(theirs, result):
    theirsIndex = ["X", "Y", "Z"].index(theirs) # X,Y,Z => 0,1,2
    relativeIndex = {"X": 2, "Y": 0, "Z": 1} #Offset by whether we lose, win, or draw
    selectedShape = ["X", "Y", "Z", "X", "Y"][theirsIndex + relativeIndex[result]] #Find our choice
    selectedShapePoints = {"X": 1, "Y": 2, "Z": 3} #Points for our choice

    resultPoints = {"X": 0, "Y": 3, "Z": 6}
    score = selectedShapePoints[selectedShape] + resultPoints[result]
    return score 

def scoreFromInput(data):
    return sum(scoreFromStrategy(*translateLine(line).split(" ")) for line in data)

if 'pyodide' in sys.modules:
    def main_day2_2():
        data = get_input('day2_2').split('\n')
        display(f"{scoreFromInput(data)= }",
            target="day2_2-output",
            append=False)

else:
    if __name__ == "__main__":
        with open('input.txt', 'r') as fp:
            data = fp.read().split('\n')
            print(f"{scoreFromInput(data)= }")