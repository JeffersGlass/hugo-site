#(get_input('day1_1').split('\n\n'))
#display(f"{max(elf_calories)= }", target="day1_1-output", append=False)

def scoreFromStrategy(theirs, mine):

    selectedShapePoints = {"X": 1, "Y": 2, "Z": 3}
    points = selectedShapePoints[mine]
    if theirs == mine: #draw
        points += 3
    elif  ((theirs, mine) == ("X", "Y") or
        (theirs, mine) == ("Y", "Z") or
        (theirs, mine) == ("Z", "X")): #win
        print("WIN")
        points += 6
    return points

def scoreFromInput(data):
    total = 0
    for line in data:
        translated_line = line.translate(str.maketrans({"A": "X", "B": "Y", "C": "Z"}))
        score = scoreFromStrategy(*translated_line.split(" "))
        print(f"{translated_line= } {score=}\n")
        total += score
    return total

if __name__ == "__main__":
    with open('input.txt', 'r') as fp:
        data = fp.read().split('\n')
        print(f"{scoreFromInput(data)= }")