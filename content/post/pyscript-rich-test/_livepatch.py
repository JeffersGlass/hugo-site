from rich.live import Live, _RefreshThread
import asyncio
from inspect import getsource

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
        self._schedule

    def _refresh_live(self) -> None:
        self.live.refresh()

    def _schedule_next(self):
        self._refresh_live()
        self.task = Pyscript.loop.create_task(asyncio.sleep(1))
        self.task.add_done_callback(self._schedule_next())

#This doesn't work - rich.Live already references the existing _RefreshThread object,
# even though this reference doesn't
_RefreshThread = Pyscript_RefreshThread
print(_RefreshThread.stop.__doc__)

