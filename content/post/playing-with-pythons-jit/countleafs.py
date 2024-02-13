import collections
import itertools
import pathlib

count = {}
path = pathlib.Path("./4_sequence_py_stats/py_stats")

for filepath in (p for p in path.iterdir() if p.is_file()):
    with open(filepath, "r", encoding='utf-8') as f:
        for line in f.readlines():
            if line.startswith("UOp Sequence Count") and line.count(",") == 3:
                index = line[len("UOp Sequence Count") + 1:].partition("]")[0]
                if index in count:
                    count[index] += 1
                else:
                    count[index] = 1

chunked = itertools.groupby(count.keys(), lambda k: ''.join(k.split(",")[:-1]))
chunks = 0
for k, g in chunked:
    chunks += 1

print(chunks)


print(len(count))