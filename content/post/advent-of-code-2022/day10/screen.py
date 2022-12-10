from typing import NamedTuple

class Screen():
    def __init__(self):
        self.lines = [['.'] * 40 for _ in range(6)]
        self.beam_position =  Position(row = 0, column = 0)

    def __str__(self):
        return '\n'.join(''.join(line) for line in self.lines)

    def tick(self, input_from_computer: int) -> None:
        if abs(self.beam_position.column - input_from_computer) <= 1:
            self.lines[self.beam_position.row][self.beam_position.column] = "#"

        next_column = self.beam_position.column + 1
        if next_column >= 40:
            next_column = 0
            next_row = self.beam_position.row + 1
        else:
            next_row = self.beam_position.row
        self.beam_position = Position(row = next_row, column = next_column)
        

class Position(NamedTuple):
    row: int
    column: int