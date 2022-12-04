import string
import sys

charValue = {s: index + 1 for index, s in enumerate(string.ascii_lowercase)} |\
            {s: index + 27 for index, s in enumerate(string.ascii_uppercase)}

def prioritySum(data):
    sum = 0    
    for line in data:
        midpoint = int(len(line)/2)
        first = set(line[:midpoint])
        second = set(line[midpoint:])
        sum += charValue[(first & second).pop()]
    return sum

def visualizeProcessing(data, tbody):    
    tbody.style.fontFamily = 'monospace'
    tbody.classList.add("unformatted-table")
    for line in data:
        row = js.document.createElement('tr')
        scoreElement = js.document.createElement('td')
        firstElement = js.document.createElement('td')
        secondElement = js.document.createElement('td')

        #styling
        row.classList.add("bg-gray-900", "text-gray-300")
        scoreElement.style.paddingRight = "2rem"
        firstElement.style.textAlign = "right"
        firstElement.style.paddingRight = "0.5rem"

        #Actually add the content
        midpoint = int(len(line)/2)
        first = line[:midpoint]
        second = line[midpoint:]
        commonChar = (set(first) & set(second)).pop()
        score = charValue[commonChar]

        first = first.replace(commonChar, f'<span style="text-shadow: 0 0 5px #ffffff; color: rgb(255, 255, 255)">{commonChar}</span>')
        second = second.replace(commonChar, f'<span style="text-shadow: 0 0 5px #ffffff; color: rgb(255, 255, 255)">{commonChar}</span>')

        #Format and insert text
        firstElement.innerHTML = "<span>" + first + "</span>"
        secondElement.innerHTML = "<span>" + second + "</span>"
        scoreElement.innerHTML = f"<span>{commonChar}={score}</span>"

        row.appendChild(scoreElement)
        row.appendChild(firstElement)
        row.appendChild(secondElement)
        tbody.appendChild(row)

    #grayRows = js.document.querySelectorAll("tbody tr:nth-child(2n-1)")
    grayRows = js.document.querySelectorAll("tr")
    for row in grayRows:
        js.console.log(row.style)
        row.style.removeProperty("background-color")

def setupTable():
    import js
    table = js.document.createElement('table')
    table.classList.add("w-full")
    tbody = js.document.createElement('tbody')
    table.appendChild(tbody)
    vizelem = js.document.getElementById("day3_1-viz")
    vizelem.classList.add("w-full")
    vizelem.classList.add("h-76")
    vizelem.classList.add("overflow-y-scroll")
    vizelem.appendChild(table)
    return tbody

if 'pyodide' in sys.modules:
    import js
    def viz_day3_1():
        tbody = setupTable()
        data = get_input('day3_1').split('\n')
        visualizeProcessing(data, tbody)
        display(f"{prioritySum(data)= }",
            target="day3_1-output",
            append=False)

elif __name__ == "__main__":
    with open("input.txt", "r") as fp:
        data = fp.read()
    result = prioritySum(data.split('\n'))
    print(f"{result= }")
