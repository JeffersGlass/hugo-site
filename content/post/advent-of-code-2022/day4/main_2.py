import sys

def overlaps(a: tuple[int, int] , b: tuple[int, int]) -> bool:
    return (a[0] <= b[0] <= a[1]) or (a[0] <= b[1] <= a[1]) or \
           (b[0] <= a[0] <= b[1]) or (b[0] <= a[1] <= b[1])

def solutionFromInput(data):
    pairs = [line.split(',') for line in data]
    pairs = [(p[0].split('-'), p[1].split('-')) for p in pairs]
    pairs = [((int(p[0][0]), int(p[0][1])), (int(p[1][0]), int(p[1][1]))) for p in pairs]
    matches = [overlaps(pair[0], pair[1]) for pair in pairs]
    return matches.count(True)

if 'pyodide' in sys.modules:
    def main_day4_2():
        data = get_input('day4_2').split('\n')
        print(data)
        display(f"{solutionFromInput(data)= }",
            target="day4_2-output",
            append=False)
else:
    if __name__ == "__main__":
        with open("input.txt", "r") as fp:
            data = fp.read().split("\n")
        print(solutionFromInput(data))
       