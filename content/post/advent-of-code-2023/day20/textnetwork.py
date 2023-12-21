from textual.app import App, ComposeResult
from textual.widgets import Header, Footer

class MyApp(App):
    BINDINGS = [("d", "toggle_dark", "Toggle Dark Mode"),
                ("escape", "exit", "Quit")]
    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()
    
    def toggle_dark(self) -> None:
        self.dark = not self.dark

if __name__ == "__main__":
    app = MyApp()
    app.run()