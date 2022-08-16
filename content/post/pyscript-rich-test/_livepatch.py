from rich.live import Live, _RefreshThread
import asyncio
from inspect import getsource

async def update_live(live: Live) -> None:
    while True:
        live.update()
        asyncio.sleep(.25)

def stop():
    task.cancel()

loop = pyscript.loop
loop.call_later(10, stop)
task = loop.create_task(update_live(live = ))

try:
    loop.run_until_complete(task)
except asyncio.CancelledError:
    pass

""" 
class Pyscript_RefreshThread():
    def __init__(self, live: "Live", refresh_per_second: float) -> None:
        self.live = live
        self.refresh_per_second = refresh_per_second
        self.done = False
        self.task = None

    def stop(self) -> None:
        "Stop the task??"
        self.task.cancel()

    def run(self) -> None:
        self._schedule_next()

    def start(self) -> None:
        self.run()

    def _refresh_live(self) -> None:
        self.live.refresh()

    def _schedule_next(self):
        self._refresh_live()
        self.task = pyscript.loop.create_task(asyncio.sleep(1))
        self.task.add_done_callback(self._schedule_next)

#This doesn't work - rich.Live already references the existing _RefreshThread object,
# even though this reference doesn't
#_RefreshThread = Pyscript_RefreshThread
#print(_RefreshThread.stop.__doc__)

def PyScript_Start(self, refresh: bool = False) -> None:
    """New start method"""
    with self._lock:
        if self._started:
            return
        self.console.set_live(self)
        self._started = True
        if self._screen:
            self._alt_screen = self.console.set_alt_screen(True)
        self.console.show_cursor(False)
        self._enable_redirect_io()
        self.console.push_render_hook(self)
        if refresh:
            try:
                self.refresh()
            except Exception:
                # If refresh fails, we want to stop the redirection of sys.stderr,
                # so the error stacktrace is properly displayed in the terminal.
                # (or, if the code that calls Rich captures the exception and wants to display something,
                # let this be displayed in the terminal).
                self.stop()
                raise
        if self.auto_refresh:
            self._refresh_thread = Pyscript_RefreshThread(self, self.refresh_per_second)
            self._refresh_thread.start()

Live.start = PyScript_Start """