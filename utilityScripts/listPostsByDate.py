import os
from pathlib import Path
import time
import re

dirpath = '../content/post'
paths = sorted(Path(dirpath).rglob('index.html'), key=os.path.getmtime)
for p in paths:
    with p.open(mode='r', encoding='utf-8') as infile:
        isDraft = re.search(r'draft:\s*true', infile.read(), re.IGNORECASE) != None
    print(f"{'DRAFT' if isDraft else '     '} {time.ctime(os.path.getmtime(p))} {p.parents[0].name}")