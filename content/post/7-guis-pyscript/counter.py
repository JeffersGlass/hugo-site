internalCount = 0
target = "counter-target"
PyScript.write(target, str(internalCount), append=False)

def add_one():
    global internalCount
    internalCount += 1
    PyScript.write(target, str(internalCount), append=False)

