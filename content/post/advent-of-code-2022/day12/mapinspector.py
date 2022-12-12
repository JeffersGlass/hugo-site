from textual.app import App, ComposeResult
from textual.widgets import Static, Label, Header, Footer, TextLog
from textual.containers import Horizontal
from textual.message import Message, MessageTarget
from textual import events

from map import Map, Cell

class MapApp(App):
    CSS_PATH = "mapinspector.css"
    def __init__(self):
        super().__init__()

        with open('inputtest.txt', 'r') as fp:
            data = fp.read().split('\n')

        self.load_map(Map(data))

    def compose(self) -> ComposeResult:
        yield Header()
        if self.map:
            for row in range(self.map.rows):
                yield Horizontal(
                    *[CellLabel(self.map.cells[(row, col)], classes="cell", id=f"c{row}-{col}") for col in range(self.map.columns)],
                    classes = "maprow"
                )
        yield TextLog(classes="infopanel", id="info")
        yield Footer()

    def load_map(self, map):
        self.map = map

        self.start = [cell for cell in self.map.cells.values() if cell.name == "S"][0]
        self.end = [cell for cell in self.map.cells.values() if cell.name == "E"][0]

        self.paths_to_investigate = [[self.start]]
        self.paths_to_finish = []
        self.dead_ends = set()

        self.refresh()

    def on_cell_label_cell_message(self, message):
        self.query_one(TextLog).write(str(message.cell))

    def _on_key(self, event: events.Key) -> None:
        if isinstance(self.focused, CellLabel):
            current_row = self.focused.cell.row
            current_column = self.focused.cell.column

            if event.key == 'left' and current_column > 0:
                self.set_focus(self.query_one(f"#c{current_row}-{current_column - 1}"))

            elif event.key == 'right' and current_column < self.map.columns - 1:
                self.set_focus(self.query_one(f"#c{current_row}-{current_column + 1}"))

            elif event.key == 'up' and current_row > 0:
                self.set_focus(self.query_one(f"#c{current_row - 1}-{current_column }"))

            elif event.key == 'down' and current_row < self.map.rows - 1:
                self.set_focus(self.query_one(f"#c{current_row + 1}-{current_column }"))

class CellLabel(Label, can_focus=True):
    def __init__(self, cell: Cell, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.cell: Cell = cell

    def compose(self):  
        yield Label(self.cell.name)

    class CellMessage(Message):
        def __init__(self, sender: MessageTarget, cell):
            self.cell = cell
            super().__init__(sender)

    async def _on_focus(self, event: events.Focus) -> None:
        await self.emit(self.CellMessage(self,self.cell))


if __name__ == "__main__":
    app = MapApp()
    app.run()