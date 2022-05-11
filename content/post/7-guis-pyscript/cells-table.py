from js import document, console
from pyodide import create_proxy
from table import Spreadsheet

columnIndices = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

document_sheet = document.getElementById("spreadsheet")

sheet = Spreadsheet()

def _handle_input_change(e):
    console.log("Processing Cell" + str(e.target.id))
    e.target.blur()

handle_input_change = create_proxy(_handle_input_change);

def _handle_cell_enter(e):
    code = e.keyCode
    if code == 13:
        _handle_input_change(e)

handle_cell_enter = create_proxy(_handle_cell_enter);

def render_table(s: Spreadsheet):
    for location, value in s.data.items():
        id = "cell-" + str(location[0]) + "-" + str(location[1])
        cell_input = document.getElementById(id)
        cell_input.value = value
        console.log(f"Attempted to set #{id} to {value}")

def create_table(num_x, num_y):
    create_header(num_x)
    create_cells(num_x, num_y)

def create_header(num_x):
    header = document.querySelector("#spreadsheet > thead")
    upperLeft = document.createElement("th")
    header.appendChild(upperLeft)
    for i in range(num_x):
        heading = document.createElement("th")
        heading.innerText = columnIndices[i]
        header.appendChild(heading)

def create_cells(num_x, num_y):
    for y in range(num_y):
        row = document.createElement("tr")
        row.classList.add("row", "overflow", "overflow-x-hidden")
        #Create row label
        cell = document.createElement("td")
        label = document.createElement("span")
        label.classList.add("w-12")
        label.innerText = y
        cell.appendChild(label)
        row.appendChild(cell)
        for x in range(num_x):
            sheet.set((columnIndices[x], y), f"{columnIndices[x]},{y}")
            cell = document.createElement("td")
            cell.classList.add("border-2", "border-gray-300", "w-48", "h-6")
            new_input = document.createElement("input")
            new_input.classList.add("w-48", "h-6")
            new_input.id=f"cell-{columnIndices[x]}-{y}"
            new_input.addEventListener("keydown", handle_cell_enter)
            new_input.addEventListener("blur", handle_input_change)
            cell.appendChild(new_input)
            row.appendChild(cell)
        document_sheet.appendChild(row)

create_table(len(columnIndices),15)
render_table(sheet)