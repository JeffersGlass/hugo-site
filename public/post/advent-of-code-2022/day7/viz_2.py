from contextlib import redirect_stdout
from io import StringIO
import sys

from anytree import Node, RenderTree, PreOrderIter
from anytree.search import findall
from anytree.render import ContStyle

def viz_day7_2():    
    def local_main(data):
        import js 

        if (root_cmd := data[0]) == "$ cd /":
            root = Node('/')
            data = data[1:]
        else: raise ValueError(f"First command something other than cd / : {root_cmd}")

        currentNode = root

        for line in data:
            currentNode = processLine_7_2(line, root, currentNode)

        # After constructing tree, pre-calculate folder sizes.
        # A bit inefficient, but fine
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
                selectedFolder = folder
                display(folder.folder_size, target="day7_2-output", append=False)
                break        

        if (pre:= js.document.getElementById("day7_2-pre")) is None:
            # Make pre tag for output
            pre = js.document.createElement("pre")
            pre.id = "day7_2-pre"
            pre.classList.add("bg-gray-900", "text-gray-300")
            pre.style.lineHeight = '1.1'
            container = js.document.getElementById("day7_2-viz")
            container.classList.add('max-h-124', 'overflow-y-auto', 'my-4')
            container.appendChild(pre)
        else:
            pre.innerHTML = "" #clear existing output

        runningTotal = 0
        for pre, fill, node in RenderTree(root, style=ContStyle()):
            #if node in small_folders:
            nameSegment = f"{pre}{node.name}"
            if hasattr(node, 'size'): displaySize = f"{'size:': >{len('folder size:')}} {str(node.size)}"
            elif hasattr(node, 'folder_size'): displaySize = f"{'folder size:'} {str(node.folder_size)}"
            else: displaySize = ''

            contents = f"{nameSegment: <60}{displaySize}"

            #Highlight solution lines
            if node == selectedFolder or (node in selectedFolder.descendants and isFile_7_2(node)):
                if node == selectedFolder: contents = f"{contents: <85} <<<<< SOLUTION"
                if isFile_7_2(node):
                    runningTotal += node.size
                    contents = f"{contents: <85} Running Total: {runningTotal}"
                contents = f'<span style="text-shadow: 0 0 8px #ffffff; color: rgb(255, 255, 255)">{contents}</span>'
            else:
                contents = f'<span>{contents}</span>'
            
            display(HTML(contents),
                    target = "day7_2-pre")
      

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

    data = get_input('day7_2').split('\n')
    local_main(data)