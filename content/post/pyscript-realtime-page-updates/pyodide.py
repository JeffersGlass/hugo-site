from js import document

print("started")

for i in range(100):
    print(i)
    document.getElementById("myDiv").textContent = i

print("finished")