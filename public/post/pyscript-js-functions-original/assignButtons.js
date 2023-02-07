buttonOutput = document.getElementById("button-output")

document.getElementById("x").addEventListener("click", () => {
    buttonOutput.innerHTML += pyodideGlobals.get('x') + "<br>"
});

document.getElementById("y").addEventListener("click", () => {
    buttonOutput.innerHTML += pyodideGlobals.get('y') + "<br>"
});

document.getElementById("z").addEventListener("click", () => {
    buttonOutput.innerHTML += pyodideGlobals.get('z') + "<br>"
});