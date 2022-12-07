import sys

from anytree import Node, RenderTree, PreOrderIter
from anytree.search import findall

def solution_7_2(data):
    if (root_cmd := data[0]) == "$ cd /":
        root = Node('/')
        data = data[1:]
    else: raise ValueError(f"First command something other than cd / : {root_cmd}")

    currentNode = root

    for line in data:
        currentNode = processLine_7_2(line, root, currentNode)

    for node in PreOrderIter(root):
        if isFolder_7_2(node) and not hasattr(node, "folder_size"):
            node.folder_size = containedFileSize_7_2(node)

    size_used = root.folder_size
    total_size = 70_000_000
    size_available = total_size - size_used

    size_needed_for_update = 30_000_000
    minimum_delete = size_needed_for_update - size_available

    # Sort folders by size, find the smallest one larger than the needed size
    for folder in sorted(findall(root, lambda n: hasattr(n, "folder_size")), key= lambda n: n.folder_size):
        if folder.folder_size > minimum_delete:
            return folder.folder_size

def processLine_7_2(line: str, rootNode: Node, currentNode: Node) -> Node:
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
            # List Files
            pass
        case ["dir", dirname]:
            # New directory {dirname}
            newDir = Node(name=dirname, parent = currentNode)
        case [size, filename]:
            # New file {filename}
            newFile = Node(name=filename, parent=currentNode, size=int(size))
        case _:
            raise ValueError(f"Somehow unmatched??")
            # Somehow unmatched??

    return nextCurrentNode

def printTree_7_2(root:Node) -> None:
    for pre, fill, node in RenderTree(root):
        print(f"{pre}{node.name}{' - ' + str(node.size) if hasattr(node, 'size') else ''}")

def isFile_7_2(node:Node) -> bool:
    return len(node.children) == 0

def isFolder_7_2(node:Node) -> bool:
    return len(node.children) > 0

def containedFileSize_7_2(node:Node) -> bool:
    if isFile_7_2(node):
        return node.size
    
    return sum(containedFileSize_7_2(n) for n in node.children)

if 'pyodide' in sys.modules:
    def main_day7_2():
        data = get_input('day7_2').split('\n')
        display(f"{solution_7_2(data)=}",
            target="day7_2-output",
            append=False)
else:
    with open("input.txt", "r") as fp:
        data = fp.read().split('\n')

    print(solution_7_2(data))