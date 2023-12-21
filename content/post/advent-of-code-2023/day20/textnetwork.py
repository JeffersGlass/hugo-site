from textual.app import App, ComposeResult
from textual.containers import ScrollableContainer, Horizontal
from textual.widgets import Header, Footer, Static
from textual.reactive import reactive

from main_2 import load_modules, push_button_2
from module import Broadcaster, Dummy, Conjunction, Counter, FlipFlop, Module
from pulse import State

class Node(Static):
    def __init__(self, m:Module, *args, **kwargs):
        super().__init__(m.label, *args, **kwargs)
        self.module = m
        self.set_classes()

    def set_classes(self):
        pass
        classes = f"{classToClass[str(type(self.module))]}"

        if type(self.module) == FlipFlop and self.module.state == State.ON: classes += " on"
        else: classes += " off"

        self.classes = classes
    
classToClass = {
    "<class 'module.Broadcaster'>" : 'broadcaster',
    "<class 'module.Dummy'>" : 'dummy',
    "<class 'module.Conjunction'>" : 'conjunction',
    "<class 'module.Counter'>" : 'counter',
    "<class 'module.FlipFlop'>" : 'flipflop'
}
class MyApp(App):
    CSS_PATH = "textnetwork.tcss"
    BINDINGS = [("d", "toggle_dark", "Toggle Dark Mode"),
                ("a", "step_list", "Process One Pulse")]
    
    def __init__(self):
        with open("input_test.txt", "r") as f:
            data = f.read().split("\n")

        self.modules = load_modules(data)
        super().__init__()
    
    def compose(self) -> ComposeResult:
        nodes = [] #
        with Horizontal():
            for label, m in self.modules.items():
                yield Node(m, id=label)

        yield Footer()
    
    def action_toggle_dark(self) -> None:
        self.dark = not self.dark

    def action_step_list(self) -> None:
        push_button_2(self.modules)
        for node in self.query(Node):
            #node.update(node.module.label)
            node.set_classes()


if __name__ == "__main__":
    app = MyApp()
    app.run()
    