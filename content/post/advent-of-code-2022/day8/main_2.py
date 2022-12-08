import sys

def solution_8_2(data: list[str]):
    max_trees_visible = 0
    high_score_location = None
    visible_from_high_score = set()

    for house_row_index, treehouse_row in enumerate(data):
        for house_col_index, treehouse_height in enumerate(treehouse_row):
        
            visible_trees = set()
            score = 1

            #Row left to right
            row_to_right = data[house_row_index][house_col_index+1:]

            visbile_from_func = find_visible_in_line_8_2(row_to_right, max_height=int(treehouse_height))
            visible_trees |= {(house_row_index, line_index + house_col_index + 1) for line_index in visbile_from_func}
            score *= len(visbile_from_func)
            
            #Rows right to left
            row_to_left = list(reversed(data[house_row_index][:house_col_index]))
            visbile_from_func = find_visible_in_line_8_2(row_to_left, max_height=int(treehouse_height))
            visible_trees |= {(house_row_index, house_col_index - 1 - line_index) for line_index in visbile_from_func}
            score *= len(visbile_from_func)

            #Columns Top to Bottom:
            column_down = [row[house_col_index] for row in data[house_row_index+1:]]
            visbile_from_func = find_visible_in_line_8_2(column_down, max_height=int(treehouse_height))
            visible_trees |= {(house_row_index + line_index + 1, house_col_index) for line_index in visbile_from_func}
            score *= len(visbile_from_func)
            
            #Columns bottom to top:
            column_up = list(reversed([row[house_col_index] for row in data[:house_row_index]]))
            visbile_from_func = find_visible_in_line_8_2(column_up, max_height=int(treehouse_height))
            visible_trees |= {(house_row_index - line_index - 1, house_col_index) for line_index in visbile_from_func}
            score *= len(visbile_from_func)

            if score > max_trees_visible:
                max_trees_visible = score
                high_score_location = (house_row_index, house_col_index)
                visible_from_high_score = visible_trees
    
    #printVisibleTrees(data, visible_from_high_score, special=high_score_location)

    return max_trees_visible


def printVisibleTrees(data: list[str], visible_trees: set[tuple[int, int]], special = None):
    for row_index, row in enumerate(data):
        for column_index, char in enumerate(row):
            if (row_index, column_index) == special:
                print(f"[black dark_slate_gray_1]{char}[/]", end = "")
            elif (row_index, column_index) in visible_trees:
                print(f"[green on dark_red]{char}[/]", end = "")
            else:
                print(f"[bright_black]{char}[/]", end = "")
        print("")

def find_visible_in_line_8_2(line: str, max_height = 9) -> int:
    #print(f"Visible in line {list(line)} from height {max_height}; ", end = "")
    visible_trees = set()

    if not line:
        #print("Nothing here, score 0")
        return visible_trees

    for line_index, tree in enumerate(line):
        if int(tree) >= max_height:
            #print(f"Score: {line_index+1}")
            return range(0, line_index+1)
    else:
        #print(f"Max length, score {len(line)}")
        return range(0, len(line))

if 'pyodide' in sys.modules:
    def main_day8_2():
        data = get_input('day8_2').split('\n')
        display(f"{solution_8_2(data)=}",
            target="day8_2-output",
            append=False)
else:
    from rich import print
    with open("input.txt", "r") as fp:
        data = fp.read().split('\n')
    
    print(f"{solution_8_2(data)=}")