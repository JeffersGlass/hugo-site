import asyncio
from rich import get_console
from rich.console import Console, RenderableType, ConsoleRenderable
from typing import Type, Optional, Callable, IO, List
from types import TracebackType
from rich.live_render import VerticalOverflowMethod

class PyscriptRefresher():
    def __init__(
        self,
        renderable: RenderableType,
        element: 'Element',
        live: 'Live',
        refresh_per_second: float = 4,
    ) -> None:
        self._renderable = renderable
        self.live = live
        self.element = element
        self.refresh_per_second = refresh_per_second
        self.done = False
        self._refresh_task = None


    async def update_live(self) -> None:
        console.log("Starting update live function")
        while True:
            console.log(f"About to write {self._renderable}")
            self.element.write(self._renderable)
            await asyncio.sleep(1/self.refresh_per_second)


    def run(self) -> bool:
        """Starts the refresh coroutine if it is not already running

        Returns:
            True if the coroutine was successfully created and started
            False if the coroutine was already running, or not successfully created
        """
        if self._refresh_task is not None:
            return False
        loop = pyscript.loop
        console.log("About to start running refresh task")
        self._refresh_task = loop.create_task(self.update_live())
        #loop.run_until_complete(self._refresh_task)

    def stop(self) -> None:
        """Stops the refresh coroutine if it is running"""
        if self._refresh_task is not None:
            self._refresh_task.cancel()
            self._refresh_task = None


class Live():
    """Renders an auto-updating live display of any given renderable.
    Mirrors the API of rich.live.LIVE

    Args:
        renderable (RenderableType, optional): The renderable to live display. Defaults to displaying nothing.
        console (Console, optional): Optional Console instance. Default will an internal Console instance writing to stdout. >>> NOT IMPLEMENTED
        auto_refresh (bool, optional): Enable auto refresh. If disabled, you will need to call `refresh()` or `update()` with refresh flag. Defaults to True >>> NOT IMPLEMENTED
        refresh_per_second (float, optional): Number of times per second to refresh the live display. Defaults to 4. >>> NOT IMPLEMENTED
        transient (bool, optional): Clear the renderable on exit (has no effect when screen=True). Defaults to False. >>> NOT IMPLEMENTED
        redirect_stdout (bool, optional): Enable redirection of stdout, so ``print`` may be used. Defaults to True. >>> NOT IMPLEMENTED
        redirect_stderr (bool, optional): Enable redirection of stderr. Defaults to True. >>> NOT IMPLEMENTED
        vertical_overflow (VerticalOverflowMethod, optional): How to handle renderable when it is too tall for the console. Defaults to "ellipsis". >>> NOT IMPLEMENTED
        get_renderable (Callable[[], RenderableType], optional): Optional callable to get renderable. Defaults to None. >>> NOT IMPLEMENTED
        element_id (str): The id of a DOM element (often a div) that the live element will be written to
        
        The screen parameters of rich.live.Live is not used
    """

    def __init__(
        self,
        renderable: Optional[RenderableType] = None,
        element_id: str = '',
        *,
        rich_console: Optional[Console] = None,
        #screen: bool attribute not used
        auto_refresh: bool = True,
        refresh_per_second: float = 4,
        transient: bool = False,
        redirect_stdout: bool = True,
        redirect_stderr: bool = True,
        vertical_overflow: VerticalOverflowMethod = "ellipsis",
        get_renderable: Optional[Callable[[], RenderableType]] = None,
        **kwargs
    ) -> None:
        assert refresh_per_second > 0, "refresh_per_second must be > 0"
        self._renderable = renderable
        self.console = rich_console if rich_console is not None else get_console()
        #self._screen = screen
        self._alt_screen = False

        self._redirect_stdout = redirect_stdout
        self._redirect_stderr = redirect_stderr
        self._restore_stdout: Optional[IO[str]] = None
        self._restore_stderr: Optional[IO[str]] = None

        #self._lock = RLock()
        self.auto_refresh = auto_refresh
        self.transient = transient

        self.vertical_overflow = vertical_overflow
        self._get_renderable = get_renderable

        assert element_id != ''
        self.element = Element(element_id)

        self.refresh_per_second = refresh_per_second
        self._refresh_thread = PyscriptRefresher(renderable = self._renderable, element = self.element, live=self, refresh_per_second = self.refresh_per_second)
        

    @property
    def is_started(self) -> bool:
        """Check if live display has been started."""
        return self._refresh_thread._refresh_task is not None

    def get_renderable(self) -> RenderableType:
        renderable = (
            self._get_renderable()
            if self._get_renderable is not None
            else self._renderable
        )
        return renderable or ""

    def start(self, refresh: bool = False) -> None:
        """Start live rendering display.

        Args:
            refresh (bool, optional): Also refresh. Defaults to False.
        """
        
        if refresh: self.element.write(self._renderable)
        self._refresh_thread.run()

    def stop(self) -> None:
        """Stop live rendering display."""
        self._refresh_thread.stop()

    def __enter__(self) -> 'Live':
        self.start(refresh=self._renderable is not None)
        return self

    def __exit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_val: Optional[BaseException],
        exc_tb: Optional[TracebackType],
    ) -> None:
        self.stop()

    def renderable(self):
        return self._renderable

    def update(self, renderable: RenderableType, *, refresh: bool = False) -> None:
        """Update the renderable that is being displayed

        Args:
            renderable (RenderableType): New renderable to use.
            refresh (bool, optional): Refresh the display. Defaults to False.
        """
        pass #Not implemented
    
    def refresh(self) -> None:
        """Update the display of the Live Render."""
        pass #not implemented

    def process_renderables(
        self, renderables: List[ConsoleRenderable]
    ) -> List[ConsoleRenderable]:
        pass #not implemented
