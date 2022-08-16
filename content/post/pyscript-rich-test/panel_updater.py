import asyncio\

while(True):
    await asyncio.sleep(1)
    my_text = Text(f'The current time is {datetime.now().strftime("%A %B %d, %I:%M:%S.%f%p"):}')
    my_text.stylize('bold', 20)
