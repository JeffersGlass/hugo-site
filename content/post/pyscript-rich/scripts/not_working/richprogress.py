from asyncio import sleep as asleep
from rich.progress import track

for i in track(range(20), description="Processing..."):
    await asleep(1)  # Simulate work being done