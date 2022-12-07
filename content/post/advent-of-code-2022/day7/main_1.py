import sys

from anytree import Node, RenderTree, PreOrderIter
from anytree.search import findall

def solution_7_1(data):
    if (root_cmd := data[0]) == "$ cd /":
        root = Node('/')
        data = data[1:]
    else: raise ValueError(f"First command something other than cd / : {root_cmd}")

    currentNode = root

    for line in data:
        currentNode = processLine_7_1(line, root, currentNode)

    # After constructing tree, pre-calculate folder sizes.
    # A bit inefficient, but fine
    for node in PreOrderIter(root):
        if isFolder_7_1(node) and not hasattr(node, "folder_size"):
            node.folder_size = containedFileSize_7_1(node)

    small_folders = findall(root, lambda n: hasattr(n, "folder_size") and n.folder_size <= 100_000)
    return sum(f.folder_size for f in small_folders)

def processLine_7_1(line: str, rootNode: Node, currentNode: Node) -> Node:
    """
    Processes one line of input; mutates the tree pointed to by rootNode,
    returns the new currentNode
    """
    nextCurrentNode = currentNode
    match line.split():
        case ["$", "cd", "/"]:
            # Move out to root
            nextCurrentNode = rootNode
        case ["$", "cd", ".."]:
            # Move out one level
            nextCurrentNode = currentNode.parent
        case ["$", "cd", dir]:
            # Move to directory {dir}
            nextCurrentNode = [child for child in currentNode.children if child.name == dir][0]
        case ["$", "ls"]:
            #list files
            pass
        case ["dir", dirname]:
            # New directory {dirname}
            newDir = Node(name=dirname, parent = currentNode)
        case [size, filename]:
            # New file {filename}
            newFile = Node(name=filename, parent=currentNode, size=int(size))
        case _:
            raise ValueError(f"Somehow unmatched??")

    return nextCurrentNode

def printTree_7_1(root:Node) -> None:
    for pre, fill, node in RenderTree(root):
        print(f"{pre}{node.name}{' - ' + str(node.size) if hasattr(node, 'size') else ''}")

def isFile_7_1(node:Node) -> bool:
    return len(node.children) == 0

def isFolder_7_1(node:Node) -> bool:
    return len(node.children) > 0

def containedFileSize_7_1(node:Node) -> bool:
    if isFile_7_1(node):
        return node.size
    
    return sum(containedFileSize_7_1(n) for n in node.children)

if 'pyodide' in sys.modules:
    pass
else:
    with open("input.txt", "r") as fp:
        data = fp.read().split('\n')

    print(solution_7_1(data))

    