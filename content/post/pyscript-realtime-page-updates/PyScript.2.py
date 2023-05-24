for i in range(100):
    print(i)
    display(i, target="myDiv", append = False)
    for j in range(1_000_000):
        _ = 1