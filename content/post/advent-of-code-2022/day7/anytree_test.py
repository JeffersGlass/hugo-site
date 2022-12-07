from anytree import Node, RenderTree
a = Node("a")
b = Node("b", parent = a)
c = Node("c", parent = a)
d = Node("d", parent = b, size = "This is data?")

for pre, fill, node in RenderTree(a):
    print(f"{pre}{node.name}{' - ' + str(node.size) if hasattr(node, 'size') else ''}")

s = "ABC"

match s:
    case "A", *_:
        print("It's ABC!")
    case _:
        print("It's not ABC!")