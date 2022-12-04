import sys

def fullyContains(a: tuple[int, int] , b: tuple[int, int]) -> bool:
    return a[0] <= b[0] and a[1] >= b[1]

if 'pyodide' in sys.modules:
    print("PYODIDE!")
else:
    if __name__ == "__main__":
        with open("input.txt", "r") as fp:
            data = fp.read().split("\n")
        pairs = [line.split(',') for line in data]
        pairs = [(p[0].split('-'), p[1].split('-')) for p in pairs]
        pairs = [((int(p[0][0]), int(p[0][1])), (int(p[1][0]), int(p[1][1]))) for p in pairs]
        matches = [fullyContains(pair[0], pair[1]) or fullyContains(pair[1],pair[0]) for pair in pairs]
        print(matches.count(True))