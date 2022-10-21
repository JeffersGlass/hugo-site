from functools import partial

def finish_in(seconds):
    if seconds <= 0:
        Element('timer-output').write("DONE!", append=True)
    else:
        Element('timer-output').write(seconds, append=True)
        PyScript.loop.call_later(1, finish_in, seconds-1)

PyScript.loop.call_soon(finish_in, 5)