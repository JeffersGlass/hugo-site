pyodide.runPythonAsync(`
    from js import document
    from asyncio import sleep

    for i in range(100):
        print(i)
        document.getElementById("myDiv").textContent = i
        await sleep(0.01) # Top level await is permitted by runPythonAsync
        for j in range(1_000_000):
            _ = 1
    `)