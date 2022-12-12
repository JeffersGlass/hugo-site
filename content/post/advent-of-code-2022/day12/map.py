import string

class Map():
    class Border():
        value = "BORDER"
    
    BORDER = Border()

    def __init__(self, lines: list[list[str]]):

        self.rows = len(lines)
        self.columns = len(lines[0])
        self.cells: dict[Cell] = {}

        for row_index, line in enumerate(lines):
            for column_index, char in enumerate(line):

                new_cell = Cell(value=char, row=row_index, column=column_index)

                if column_index == 0: new_cell.left = Map.BORDER
                else:
                    new_cell.left = self.cells[(row_index, column_index -1)]
                    new_cell.left.right = new_cell

                if column_index == len(line) - 1: new_cell.right = Map.BORDER
                
                if row_index == 0: new_cell.up = Map.BORDER
                else:
                    new_cell.up = self.cells[(row_index - 1, column_index)]
                    new_cell.up.down = new_cell 
                
                if row_index == len(lines) - 1:
                    new_cell.down = Map.BORDER

                self.cells[(row_index, column_index)] = new_cell
        
    def __str__(self):
        row_list = []
        for row in range(self.rows):
            for col in range(self.columns):
                row_list.append(self.cells[(row, col)].value)

            row_list.append('\n')
        return ''.join(row_list)

class Cell():
    def __init__(self, value, row = None, column = None, up = None, left = None, right = None, down = None):
        self.name = value
        if value == 'S': self.value = 1
        elif value == 'E': self.value = 26
        else: self.value = string.ascii_lowercase.index(value) + 1
        self.row = row
        self.column = column
        self.up = up 
        self.left = left
        self.down = down
        self.right = right
        
    def __str__(self):
        return f"Cell {self.location}. Value: {self.value} Up:{self.up.value if self.up else 'NONE'} Left:{self.left.value if self.left else 'NONE'} Down:{self.down.value if self.down else 'NONE'} Right:{self.right.value if self.right else 'NONE'}"

    def __repr__(self):
        return str(self)

    @property
    def location(self):
        return (self.row, self.column)

    @property
    def neighbors(self):
        return [n for n in (self.up, self.left, self.down, self.right) if n is not Map.BORDER]