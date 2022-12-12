from textual.app import App, ComposeResult
from textual.widgets import Static, Label, Header, Footer, TextLog
from textual.containers import Horizontal, Vertical
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
            yield Vertical(
                *(
                    Horizontal(
                        *[CellLabel(self.map.cells[(row, col)], classes="cell", id=f"c{row}-{col}") for col in range(self.map.columns)],
                        classes = "maprow"
                    )  for row in range(self.map.rows)
                 ), classes = "map"
            )
        yield TextLog(classes="infopanel", id="info")
        yield TextLog(id="cellpanel")
        yield Footer()

    def load_map(self, map):
        self.map: Map = map

        self.start: Cell = [cell for cell in self.map.cells.values() if cell.name == "S"][0]
        self.end: Cell = [cell for cell in self.map.cells.values() if cell.name == "E"][0]

        self.paths_to_investigate = [[self.start]]
        self.paths_to_finish = []
        self.dead_ends = set()

        self.refresh()  

        self.iterate_path_one_step(self.paths_to_investigate.pop())
        self.show_path(self.paths_to_investigate[-1])

        self.refresh()

    def show_path(self, current_path):
        for cell_label in self.query(CellLabel):
            cell_label.remove_class('active', 'path')
            if any([cell_label.cell.location == pathnode.location for pathnode in current_path]):
                cell_label.add_class('path')
            if cell_label.cell.location == current_path[-1].location:
                cell_label.add_class('active')

    def iterate_path_one_step(self, current_path):
        current_cell = current_path[-1]

        if current_cell == self.end:
            
            self.paths_to_finish.append(current_path)
            return

        new_neighbors = self.get_valid_neighbors(current_cell, self.dead_ends, self.end)

        if not new_neighbors:
            self.dead_ends.add(current_cell)
            return

        for n in new_neighbors:
            self.paths_to_investigate.append(current_path + [n])
    
    def get_valid_neighbors(self, cell, dead_ends, end):
        return [n for n in cell.neighbors if n not in dead_ends and n != end]

    def on_cell_label_cell_message(self, message):
        self.clear_celldisplay()
        self.showcell(str(message.cell))

    def _on_key(self, event: events.Key) -> None:
        self.show_path(self.paths_to_investigate[-1])
        if event.key == 'enter':
            self.iterate_path_one_step(self.paths_to_investigate.pop())
            self.show_path(self.paths_to_investigate[-1])
            self.writelog(self.paths_to_investigate[-1])

        elif isinstance(self.focused, CellLabel):
            current_row = self.focused.cell.row
            current_column = self.focused.cell.column

            moved = False
            if event.key == 'left' and current_column > 0:
                self.set_focus(self.query_one(f"#c{current_row}-{current_column - 1}"))
                moved = True
            elif event.key == 'right' and current_column < self.map.columns - 1:
                self.set_focus(self.query_one(f"#c{current_row}-{current_column + 1}"))
                moved = True
            elif event.key == 'up' and current_row > 0:
                self.set_focus(self.query_one(f"#c{current_row - 1}-{current_column }"))
                moved = True
            elif event.key == 'down' and current_row < self.map.rows - 1:
                self.set_focus(self.query_one(f"#c{current_row + 1}-{current_column }"))
                moved = True
            if moved:
                self.showcell(self.focused.cell)

    def clearlog(self):
        self.query_one("#info", TextLog).clear()
        self.refresh()

    def writelog(self, s):
        self.query_one("#info", TextLog).write(s)

    def clear_celldisplay(self):
        self.query_one("#cellpanel", TextLog).clear()

    def showcell(self, cell):
        self.query_one("#cellpanel", TextLog).write(cell)

class CellLabel(Label, can_focus=True):
    def __init__(self, cell: Cell, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.cell: Cell = cell

    def compose(self):  
        l = Label(self.cell.label)
        yield Label(self.cell.label)

    class CellMessage(Message):
        def __init__(self, sender: MessageTarget, cell):
            self.cell = cell
            super().__init__(sender)

    async def _on_focus(self, event: events.Focus) -> None:
        await self.emit(self.CellMessage(self,self.cell))


if __name__ == "__main__":
    app = MapApp()
    app.run()