import os
from typing import List

def visualize_project(path: str, display: str):
    # Check if path is valid
    if not os.path.exists(path):
        raise ValueError("Invalid path")

    # Get list of files and directories in project
    items = os.listdir(path)

    if display == "tree":
        # Print a tree representation of the project
        print_tree(items, 0)
    elif display == "diagram":
        # Print a diagram representation of the project
        print_diagram(items)
    else:
        # Print an error message
        print("Invalid display type")

def print_tree(items: List[str], indent: int):
    for item in items:
        # Print the item name with the appropriate indentation
        print(" " * indent + item)

        # If the item is a directory, recursively print its contents
        if os.path.isdir(item):
            print_tree(os.listdir(item), indent + 2)

def print_diagram(items: List[str]):
    # TODO: Print a diagram representation of the project using icons and colors
    pass

# Example usage
visualize_project("./", "tree")
visualize_project("./", "diagram")
