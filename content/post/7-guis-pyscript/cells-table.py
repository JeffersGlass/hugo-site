from js import document, console
from pyodide import create_proxy
from spreadsheet import Spreadsheet
import re

columnIndices = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

document_sheet = document.getElementById("spreadsheet")

sheet = Spreadsheet()

def _handle_input_change(e):
    console.log("Processing Cell" + str(e.target.id))
    render_table(sheet)

def _handle_cell_enter(e):
    code = e.keyCode
    if code == 13:
        e.target.blur()

def _handle_cell_blur(e):
    column = re.search(r'cell-(\w)-(\d+)', e.target.id).group(1)
    row = re.search(r'cell-(\w)-(\d+)', e.target.id).group(2)
    sheet.set((column, row), e.target.value)
    _handle_input_change(e)

handle_cell_enter = create_proxy(_handle_cell_enter)
handle_input_blur = create_proxy(_handle_cell_blur)

def _handle_cell_focus(e):
    console.log(str(e.target.id) + " gained focus")
    _handle_input_change(e)

handle_cell_focus = create_proxy(_handle_cell_focus)

def render_table(s: Spreadsheet):
    for location in s.data:
        id = "cell-" + str(location[0]) + "-" + str(location[1])
        cell_input = document.getElementById(id)
        if cell_input == document.activeElement: 
            cell_input.value = s.getRawValue(location)
        else:
            cell_input.value = s.getRenderedValue(location)

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
        label = document.createElement("div")
        label.classList.add("w-full", "font-bold", "text-right", "px-2")
        label.innerText = y
        cell.appendChild(label)
        row.appendChild(cell)

        for x in range(num_x):
            sheet.set((columnIndices[x], y), "="+str(x)+"+"+str(y))
            cell = document.createElement("td")
            cell.classList.add("border-2", "border-gray-300", "w-48", "h-6")
            new_input = document.createElement("input")
            new_input.classList.add("w-48", "h-6")
            new_input.id=f"cell-{columnIndices[x]}-{y}"
            new_input.addEventListener("keydown", handle_cell_enter)
            new_input.addEventListener("blur", handle_input_blur)
            new_input.addEventListener("focus", handle_cell_focus)
            cell.appendChild(new_input)
            row.appendChild(cell)
        document_sheet.appendChild(row)

create_table(len(columnIndices),15)
render_table(sheet)