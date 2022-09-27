"""
Demonstrates how to display a tree of files / directories with the Tree renderable.
Example (lightly) adapted from https://github.com/Textualize/rich/blob/master/examples/tree.py
"""

import os
import pathlib
import sys

from rich.filesize import decimal
from rich.markup import escape
from rich.text import Text
from rich.tree import Tree

#Adapted from rich/examples/tree.py
#Added max_steps paramters to limit tree depth
def walk_directory(directory: pathlib.Path, tree: Tree, max_depth = -1) -> None:
    """Recursively build a Tree with directory contents."""
    # Sort dirs first then by filename
    if max_depth == 0:
        tree.add("...")
        return
    paths = sorted(
        pathlib.Path(directory).iterdir(),
        key=lambda path: (path.is_file(), path.name.lower()),
    )
    for path in paths:
        # Remove hidden files
        if path.name.startswith("."):
            continue
        if path.is_dir():
            style = "dim" if path.name.startswith("__") else ""
            branch = tree.add(
                f"{escape(path.name)}",
                style=style,
                guide_style=style,
            )
            walk_directory(path, branch, max_depth-1)
        else:
            text_filename = Text(path.name, "green")
            text_filename.highlight_regex(r"\..*$", "bold red")
            text_filename.stylize(f"{path}")
            file_size = path.stat().st_size
            text_filename.append(f" ({decimal(file_size)})", "blue")
            icon = "🐍 " if path.suffix == ".py" else "📄 "
            tree.add(Text(icon) + text_filename)

directory = '/lib/python3.10'

tree = Tree(
    f"{directory}",
    guide_style="bold bright_blue",
)
walk_directory(pathlib.Path(directory), tree, max_depth = 3)
print(tree)