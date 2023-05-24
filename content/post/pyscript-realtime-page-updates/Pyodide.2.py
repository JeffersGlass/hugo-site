for i in range(100):
    print(i)
    document.getElementById("myDiv").textContent = i
    for j in range(1_000_000):
        _ = 1