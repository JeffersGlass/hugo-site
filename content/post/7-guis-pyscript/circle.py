from js import document, console, window
from math import pi, sqrt
from pyodide import create_proxy
from random import randint
from dataclasses import dataclass, field

canvas = document.getElementById("circle-canvas")
ctx = canvas.getContext("2d")
#Fill background with white
ctx.fillStyle = "white"
ctx.fillRect(0,0, canvas.width, canvas.height)

@dataclass
class Circle():
    x: int
    y: int
    radius: int

@dataclass
class UndoQueue:
    index : int
    q : list() = field(default_factory = list)

@dataclass
class ResizeOperation:
    circle: Circle
    previous_size: int
    new_size: int

uq = UndoQueue(index = -1)
currentResize = ResizeOperation(None, 0, 0)

my_circles = list()
closest_circle_index = -1

def _clear_screen():
    ctx.fillStyle = "white"
    ctx.fillRect(0,0, canvas.width, canvas.height)

def _draw_circle(x, y, radius):
    ctx.beginPath();
    ctx.arc(x, y, radius, 0, 2*pi)
    ctx.stroke()

def _draw_filled_circle(x, y, radius):
    console.log(f"Drawing filled circle at {x}, {y}, with radius {radius}")
    
    ctx.beginPath();
    ctx.arc(x, y, radius, 0, 2*pi)
    ctx.fillStyle = "gray"
    ctx.fill()

def _redraw_all():
    _clear_screen()
    if len(my_circles):
        if closest_circle_index >= 0:
            c = my_circles[closest_circle_index]
            _draw_filled_circle(c.x, c.y, c.radius)
        for c in my_circles:
            _draw_circle(c.x, c.y, c.radius)

def _make_new_circle(x, y, radius):
    new_circle = Circle(x, y, radius)
    my_circles.append(new_circle)

    uq.q = uq.q[:uq.index+1]
    uq.q.append(new_circle)
    uq.index = len(uq.q) - 1
    console.log(f"{uq}")


def _on_click(e):
    global my_circles
    console.log(str(e.offsetX) + " " + str(e.offsetY))
    if (document.getElementById("right-click-menu").style.display == "block"): _hide_menu(e)
    if e.button == 0: #left mouse button
        _make_new_circle(e.offsetX,e.offsetY, randint(40, 70))
        _redraw_all()
    else:
        #if (document.getElementById("right-click-menu").style.display == "block"): _hide_menu(e)
        if closest_circle_index >= 0: _show_menu(e)
        e.preventDefault()
        e.stopPropagation()
        return False

def _no_context(e):
    e.preventDefault()
    e.stopPropagation()
    return False

canvas.oncontextmenu = _no_context
document.getElementById("right-click-menu").oncontextmenu = _no_context

def _show_menu(event):
    console.log("Right mouse button clicked, showing menu")
    menu = document.getElementById("right-click-menu")
    menu.style.display = "block"
    menu.style.left = str(event.pageX) + "px"
    menu.style.top = str(event.pageY) + "px"

    c = my_circles[closest_circle_index]

    label = document.getElementById("circle-slider-label")
    label.innerText = f"Adjust diameter of Circle at ({c.x}, {c.y})"

    slider = document.getElementById("circle-slider")
    slider.value = my_circles[closest_circle_index].radius
    global currentResize
    currentResize.previous_size = slider.value
    currentResize.circle = c

def _change_radius(_):
    slider = document.getElementById("circle-slider")
    new_radius = slider.value
    my_circles[closest_circle_index].radius = new_radius
    _redraw_all()
    

def _hide_menu(e):
    slider = document.getElementById("circle-slider")
    global currentResize
    currentResize.new_size = slider.value

    uq.q = uq.q[:uq.index+1]
    uq.q.append(currentResize)
    uq.index = len(uq.q) - 1

    currentResize = ResizeOperation(None, 0, 0)
    document.getElementById("right-click-menu").style.display = "none"
    _recalc_nearest_circle(e.offsetX, e.offsetY)
        
def _on_move(e):
    #Do not reselect circle when menu is open
    if document.getElementById("right-click-menu").style.display == "block": return 
    if len(my_circles):
        _recalc_nearest_circle(e.offsetX, e.offsetY)

def _recalc_nearest_circle(mouse_x, mouse_y):
        closest_index = -1
        closest_distance = 1000000
        for i, c in enumerate(my_circles):
            dist = sqrt((mouse_x - c.x) ** 2 + (mouse_y - c.y) ** 2)
            if dist < closest_distance: 
                closest_index = i
                closest_distance = dist
        
        global closest_circle_index
        if closest_index != closest_circle_index:
            closest_circle_index = closest_index
            _redraw_all()

on_click = create_proxy(_on_click)
on_move = create_proxy(_on_move)
change_radius = create_proxy(_change_radius)

document.getElementById("circle-canvas").addEventListener("mousedown", on_click)
document.getElementById("circle-canvas").addEventListener("mousemove", on_move)
document.getElementById("circle-slider").addEventListener("input", change_radius)

def _press_undo(e):
    if uq.index < 0:
        console.log(f"Nothing more to undo\r\n{uq}")
        return

    op_to_undo = uq.q[uq.index]
    if type(op_to_undo) == Circle:
        my_circles.pop()
        uq.index -= 1
        if len(my_circles):
            _recalc_nearest_circle(250, 500) #A hack, bottom of the canvas
        _redraw_all()
    elif type(op_to_undo) == ResizeOperation:
        op_to_undo.circle.radius = op_to_undo.previous_size
        uq.index -= 1
        _redraw_all()
    console.log(f"After Undo {uq}\r\n{my_circles}")

def _press_redo(e):
    console.log(f"REDO {uq}\r\n{my_circles}")
    if uq.index == len(uq.q) - 1: 
        console.log(f"Nothing more to redo\r\n{uq}")
        return

    op_to_redo = uq.q[uq.index+1]
    if type(op_to_redo) == Circle:
        my_circles.append(Circle(op_to_redo.x, op_to_redo.y, op_to_redo.radius))
        uq.index += 1
    elif type(op_to_redo) == ResizeOperation:
        op_to_redo.circle.radius = op_to_redo.new_size
        uq.index += 1
    if len(my_circles):
        _recalc_nearest_circle(250, 500)   

    _redraw_all()
    console.log(f"After Redo {uq}\r\n{my_circles}")


press_undo = create_proxy(_press_undo)
press_redo = create_proxy(_press_redo)

document.getElementById("undo").addEventListener("click", press_undo)
document.getElementById("redo").addEventListener("click", press_redo)