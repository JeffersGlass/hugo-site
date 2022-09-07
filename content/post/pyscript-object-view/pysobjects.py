import html
from functools import partial
from uuid import uuid4

from js import document, console
from pyodide import create_proxy, to_js

#ensure we refresh the object display whenever shift-enter is pressed
def addDisplayToAll(event):
    if (event.shiftKey and event.key == 'Enter'):
        _displayObjects()

document.addEventListener('keydown', create_proxy(addDisplayToAll))   

#SVG Icon for Expanded Variable controls:
svg_tag_start = '''<svg'''
svg_tag_end = ''' width="16px" height="16px" viewBox="0 0 16 16" xmlns="http://www.w3.org/2000/svg" fill="currentColor" class="inline-block transition-transform duration-150"><path d="M5.56 14L5 13.587V2.393L5.54 2 11 7.627v.827L5.56 14z"/></svg>'''

#method for hiding and unhiding member attributes
def hide_unhide(event, **kwargs):
    source_id = event.currentTarget.id
    console.log(f"Source: {source_id}")
    content = str(document.getElementById(source_id).attributes.getNamedItem("data").value)
    console.log(content)

    el = document.getElementById(str(content))
    if el.classList.contains('hidden'):
        el.classList.remove('hidden')
        document.getElementById(str(source_id)).classList.add('rotated')
    else:
        el.classList.add('hidden')
        document.getElementById(str(source_id)).classList.remove('rotated')

_initial_globals = set(globals())

def _displayObjects(*args, **kwargs):
    globalObjects = (item for item in globals().items() if item[0] not in _initial_globals and item[0] not in ("_initial_globals", "_displayObjects", "_run_btn"))

    document.getElementById("global-object-output").innerHTML = ""

    for i, (variable, obj) in enumerate(globalObjects):
        svg_id = str(uuid4())
        content_id = str(uuid4())

        #Determine if we have object attributes to display as a dropdown
        try: 
            vars(obj)
        except TypeError as err:
            hasdict = False
        else:
            #only if vars is not false, i.e. not an empty container
            #And not all methods are dunder
            hasdict = bool(vars(obj)) and any(k[:2] != "__" for k in vars(obj))

        if hasdict:
            svg_tag = svg_tag_start + ' id="' + str(svg_id) + '" data= "' + content_id + '" ' + svg_tag_end
            console.log(svg_tag)
        else: svg_tag = ""

        #Alternate white and blue backgrounds per row
        if not i % 2: style = "bg-white"
        else: style = "bg-blue-50"

        #Insert row into display
        document.getElementById("global-object-output").innerHTML += f"""
        <div class="{style} font-bold">{variable} {svg_tag}</div>
        <div class="{style}">{html.escape(str(type(obj)))}</div>
        <div class="{style}">{html.escape(str(obj))}</div>
        <div class="{style}">{id(obj)}</div>
        """

        #Show subobjects if applicable
        if hasdict:
            content_to_add = f"""<div class="grid hidden grid-cols-4 col-span-4" id ="{content_id}">"""
            for j, key in enumerate(k for k in obj.__dict__ if k[:2] != "__"):
                if not i % 2:
                    if j % 2: substyle = "bg-gray-100"
                    else: substyle = "bg-gray-50"
                else:
                    if j % 2: substyle = "bg-blue-100"
                    else: substyle = "bg-blue-200"
                content_to_add += f"""
                        <div class="{substyle} text-sm">{variable}.{key}</div>
                        <div class="{substyle} text-sm">{html.escape(str(type(obj.__dict__[key])))}</div>
                        <div class="{substyle} text-sm">{html.escape(str(obj.__dict__[key]))}</div>
                        <div class="{substyle} text-sm">{id(obj.__dict__[key])}</div>
                    """
            content_to_add += """</div>"""

            document.getElementById("global-object-output").innerHTML += content_to_add
                    
            console.log(f"Adding event to svg with id {svg_id}")
            #document.getElementById(str(svg_id)).addEventListener("click", create_proxy(hide_unhide))

    #Add action to show and hide attributes as applicable
    for svg in document.getElementsByTagName("svg"):
        svg.addEventListener("click", create_proxy(hide_unhide))

    #All REPL run buttons should regenerate global objects
    for _run_btn in document.querySelectorAll('[id^="btnRun"]'):
        _run_btn.addEventListener("click", create_proxy(_displayObjects))

_displayObjects()