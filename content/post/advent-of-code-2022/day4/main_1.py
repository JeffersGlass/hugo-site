import sys

def fullyContains(a: tuple[int, int] , b: tuple[int, int]) -> bool:
    return a[0] <= b[0] and a[1] >= b[1]

def solutionFromInput(data):
    pairs = [line.split(',') for line in data]
    pairs = [(p[0].split('-'), p[1].split('-')) for p in pairs]
    pairs = [((int(p[0][0]), int(p[0][1])), (int(p[1][0]), int(p[1][1]))) for p in pairs]
    matches = [fullyContains(pair[0], pair[1]) or fullyContains(pair[1],pair[0]) for pair in pairs]
    return matches.count(True)

if 'pyodide' in sys.modules:
    def main_day4_1():
        data = get_input('day4_1').split('\n')
        display(f"{solutionFromInput(data)= }",
            target="day4_1-output",
            append=False)
else:
    if __name__ == "__main__":
        with open("input.txt", "r") as fp:
            data = fp.read().split("\n")
        print(solutionFromInput(data))
       