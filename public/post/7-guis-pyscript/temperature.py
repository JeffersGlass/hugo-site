from js import document

#This is necessary for reasons I don't understand
from pyodide import create_proxy

write_in_progress = False

def isTemp(input_temp):
    try:
        _ = float(input_temp)
    except Exception as err:
        return False
    
    return True

def _f(self, *args, **kwargs):
    global write_in_progress
    if write_in_progress:
        return
    else:
        write_in_progress = True
        f_input = document.getElementById("f-temp")
        c_output = document.getElementById("c-temp")
        input_value = f_input.value
        if isTemp(input_value):
            c_output.value = round((int(float(input_value)) - 32) * (5/9), 2)
        else:
            c_output.value = ""
        write_in_progress = False

def _c(self, *args, **kwargs):
    global write_in_progress
    if write_in_progress:
        return
    else:
        write_in_progress = True
        c_input = document.getElementById("c-temp")
        f_output = document.getElementById("f-temp")
        input_value = c_input.value
        if isTemp(input_value):
            f_output.value = round((int(float(input_value)) * (9/5)) + 32, 2)
        else:
            f_output.value = ""
        write_in_progress = False

f_change = create_proxy(_f)
c_change = create_proxy(_c)

document.querySelector("#f-temp").addEventListener("input", f_change)
document.querySelector("#c-temp").addEventListener("input", c_change)