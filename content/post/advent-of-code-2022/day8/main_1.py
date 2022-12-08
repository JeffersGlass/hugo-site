import sys

def solution_8_1(data: list[str]):
    
    # (rowIndex, columnIndex)
    visible_trees: set[tuple[int, int]] = set()

    #Rows left to right
    for row_index, row in enumerate(data):
        visible_trees |= {(row_index, line_index) for line_index in find_visible_in_line(row)}
        pass

    #Rows right to left
    for row_index, row in enumerate([row[::-1] for row in data]):
        visible_trees |= {(row_index, len(row) - line_index - 1) for line_index in find_visible_in_line(row)}
        pass

    #Columns Top to Bottom:
    for column_index in range(len(data[0])):
        column = [row[column_index] for row in data]
        visible_trees |= {(row_index, column_index) for row_index in find_visible_in_line(column)}

    #Columns Bottom to Top:
    for column_index in range(len(data[0])):
        column = [row[column_index] for row in data][::-1]
        visible_trees |= {(len(column) - row_index - 1, column_index) for row_index in find_visible_in_line(column)}
        
    printVisibleTrees(data, visible_trees)
    return(f"{len(visible_trees)= }")


def printVisibleTrees(data: list[str], visbile_trees: set[tuple[int, int]]):
    for row_index, row in enumerate(data):
        for column_index, char in enumerate(row):
            if (row_index, column_index) in visbile_trees:
                print(f"[green on dark_red]{char}[/]", end = "")
            else:
                print(f"[bright_black]{char}[/]", end = "")
        print("")

def find_visible_in_line(line: str) -> set[int]:
    max_height_seen = -1
    visible_in_line = set()

    for line_index, tree in enumerate(line):
        if int(tree) > max_height_seen:
            visible_in_line.add(line_index)
            max_height_seen = int(tree)
            if max_height_seen == 9: break

    return visible_in_line     

if 'pyodide' in sys.modules:
    pass
else:
    from rich import print
    with open("input.txt", "r") as fp:
        data = fp.read().split('\n')
    
    print(f"{solution_8_1(data)=}")