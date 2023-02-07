document.getElementById("printGlobals").addEventListener("click", () => {
    console.warn("Clicked print globals")
    document.getElementById("globals").innerHTML = pyodideGlobals;
});