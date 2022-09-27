import rich
from js import createJSObject, console, document
from js import console as jsconsole
from pyodide import create_proxy
from io import StringIO

def get_object_info_html(object_as_string, import_string, api_link=None):
    jsconsole.warn(f"GETTING OBJECT INFO FOR {object_as_string}")

    exec(import_string)
    obj = eval(object_as_string)

    temp_con = rich.console.Console(file=StringIO(), record=True)
    temp_con.print(obj.__doc__.split('\n')[0])
    #rich.inspect(obj, console=temp_con)
    #result = temp_con.file.getvalue()
    result = temp_con.export_html()

    parent = document.getElementById("docs")
    while parent.firstChild != None:
        parent.removeChild(parent.firstChild)
    
    newElement = document.createElement('div')
    newElement.innerHTML = result
    parent.appendChild(newElement)

    parent = document.getElementById("api-link")
    while parent.firstChild != None:
        parent.removeChild(parent.firstChild)

    if api_link is not None:
        link = document.createElement('a')
        link.innerHTML = '<span>API</span><img src="/svg/externallink.svg" alt="" class="inline-block h-4">'
        link.href = api_link
        link.target = "_blank"
        document.getElementById("api-link").appendChild(link)
        jsconsole.warn("api_link created")
    else:
        jsconsole.warn("no api link provided")

    jsconsole.warn(result)
    jsconsole.warn("OBJECT INFO DONE")

def clear_object_info():
    parent = document.getElementById("api-link")
    while parent.firstChild != None:
        parent.removeChild(parent.firstChild)
        
    parent = document.getElementById("docs")
    while parent.firstChild != None:
        parent.removeChild(parent.firstChild)

createJSObject(create_proxy(get_object_info_html), "get_object_info_html")
createJSObject(create_proxy(clear_object_info), "clear_object_info")

