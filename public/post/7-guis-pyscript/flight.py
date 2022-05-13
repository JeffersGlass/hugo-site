from js import document
#This is necessary for reasons I don't understand
from pyodide import create_proxy

def _flight_mode_change(*args, **kwargs):
    currentMode = document.getElementById("flight-mode-select").value
    if currentMode == 'one':
        document.getElementById("ret").disabled = True
    else:
        document.getElementById("ret").disabled = False

flight_mode_change = create_proxy(_flight_mode_change)
document.getElementById("flight-mode-select").addEventListener("input", flight_mode_change)

def _book_flight(*args, **kwargs):
    currentMode = document.getElementById("flight-mode-select").value
    departure = document.getElementById("dep").value
    return_flight = document.getElementById("ret").value

    if currentMode == 'one':
        document.getElementById("flight-info").innerText = f"You've booked a one-way flight departing on {departure}."
    else:
        document.getElementById("flight-info").innerText = f"You've booked a round-trip flight departing on {departure} and returning on {return_flight}."

book_flight = create_proxy(_book_flight)
document.getElementById("book-flight").addEventListener("click", book_flight)

flight_mode_change()
