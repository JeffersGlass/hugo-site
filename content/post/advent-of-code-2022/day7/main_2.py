import sys

from anytree import Node, RenderTree, PreOrderIter
from anytree.search import findall

DEBUG = False

def debug(*args, **kwargs):
    if DEBUG: print(*args, **kwargs)

def solution_7_1(data):
    if (root_cmd := data[0]) == "$ cd /":
        root = Node('/')
        data = data[1:]
    else: raise ValueError(f"First command something other than cd / : {root_cmd}")

    currentNode = root

    for line in data:
        currentNode = processLine(line, root, currentNode)

    for node in PreOrderIter(root):
        if isFolder(node) and not hasattr(node, "folder_size"):
            node.folder_size = containedFileSize(node)

    size_used = root.folder_size
    total_size = 70_000_000
    size_available = total_size - size_used
    size_needed_for_update = 30_000_000
    minimum_delete = size_needed_for_update - size_available
    print(f"{minimum_delete=}")
    for folder in sorted(findall(root, lambda n: hasattr(n, "folder_size")), key= lambda n: n.folder_size):
        if folder.folder_size > minimum_delete:
            return folder.folder_size

def processLine(line: str, rootNode: Node, currentNode: Node) -> Node:
    """
    Processes one line of input; mutates the tree pointed to by rootNode,
    returns the new currentNode
    """
    debug(f"{line: <30}", end = "")
    nextCurrentNode = currentNode
    match line.split():
        case ["$", "cd", "/"]:
            debug("Move out to root")
            nextCurrentNode = rootNode
        case ["$", "cd", ".."]:
            debug("Move out one level")
            nextCurrentNode = currentNode.parent
        case ["$", "cd", dir]:
            debug(f"Move to directory {dir}")
            nextCurrentNode = [child for child in currentNode.children if child.name == dir][0]
        case ["$", "ls"]:
            debug("List Files")
        case ["dir", dirname]:
            debug(f"New directory {dirname}")
            newDir = Node(name=dirname, parent = currentNode)
        case [size, filename]:
            debug(f"New file {filename}")
            newFile = Node(name=filename, parent=currentNode, size=int(size))
        case _:
            debug(f"Somehow unmatched??")

    return nextCurrentNode

def printTree(root:Node) -> None:
    for pre, fill, node in RenderTree(root):
        print(f"{pre}{node.name}{' - ' + str(node.size) if hasattr(node, 'size') else ''}")

def isFile(node:Node) -> bool:
    return len(node.children) == 0

def isFolder(node:Node) -> bool:
    return len(node.children) > 0

def containedFileSize(node:Node) -> bool:
    if isFile(node):
        return node.size
    
    return sum(containedFileSize(n) for n in node.children)

if 'pyodide' in sys.modules:
    pass
else:
    with open("input.txt", "r") as fp:
        data = fp.read().split('\n')

    print(solution_7_1(data))

    