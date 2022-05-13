from js import console
from pyodide import create_proxy
from dataclasses import dataclass, field
from collections import UserList
from random import randint

@dataclass(order=True)
class Entry():
    surname: str    
    firstname: str
    

class EntryList(UserList):
    def append(self, other):
        super().append(other)
        self.data = sorted(self.data)

entries = EntryList()

def _get_namefields():
    first = document.getElementById("firstname-input").value
    sur = document.getElementById("surname-input").value
    return first, sur

def _update_view():
    console.log("Updating listbox view")
    list = document.getElementById("listbox")
    list.innerHTML = ""

    filter_text = document.getElementById("filter-input").value
    if filter_text == "": filter = None
    else: filter = filter_text

    for entry in entries:
        if filter is None or entry.surname.startswith(filter):
            option = document.createElement('option')
            option.value = entry.firstname + ", " + entry.surname
            option.text = entry.firstname + ", " + entry.surname
            list.appendChild(option)

def _create_entry(*args, **kwargs):
    console.log("Create clicked")
    first, sur = _get_namefields()
    new_entry = Entry(firstname = first, surname = sur)
    entries.append(new_entry)
    _update_view()

def _delete_entry(*args, **kwargs):
    console.log("Delete clicked")
    list = document.getElementById("listbox")
    index = list.selectedIndex
    
    if index >= 0:
        entries.pop(index)
        _update_view()

def _update_entry(*args, **kwargs):
    list = document.getElementById("listbox")
    index = list.selectedIndex

    if index >= 0:
        entries.pop(index)
        _create_entry()

def _filter_key(*args, **kwargs):
    console.log("Filter input changed")
    _update_view()

create_entry = create_proxy(_create_entry)
delete_entry = create_proxy(_delete_entry)
update_entry = create_proxy(_update_entry)
filter_key = create_proxy(_filter_key)

document.getElementById("create").addEventListener("click", create_entry)
document.getElementById("delete").addEventListener("click", delete_entry)
document.getElementById("update").addEventListener("click", update_entry)

document.getElementById("filter-input").addEventListener("input", filter_key)