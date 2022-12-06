"""
Improvements:
- File size
- File last modification date
- Code statistics
"""

import os

# Map file extensions to file type icons
file_icons = {
    ".py": "🐍",
    ".js": "🐢",
    ".rb": "🦀",
    ".java": "☕️",
    ".go": "🐹",
    ".c": "🐦",
    ".cpp": "🐦🐦",
    ".h": "🐦🦜",
    ".txt": "📝",
    ".md": "📚",
    ".pdf": "📎",
    ".zip": "🗜️",
    ".exe": "⚙️",
    ".sh": "🐚",
}

# Map file types to color codes
file_colors = {
    "script": "\033[94m",
    "source": "\033[92m",
    "text": "\033[93m",
    "binary": "\033[91m",
}

# Root directory of the code project
root_dir = "./"

# Print the project tree
for root, dirs, files in os.walk(root_dir):
    # Print the current directory
    print(f"{root}:")

    # Print the files in the current directory
    for file in files:
        # Get the file's extension
        ext = os.path.splitext(file)[1]

        # Get the file's icon
        icon = file_icons.get(ext, "❓")

        # Get the file's type
        if ext in file_icons:
            if ext in [".py", ".js", ".rb", ".sh"]:
                file_type = "script"
            elif ext in [".java", ".go", ".c", ".cpp", ".h"]:
                file_type = "source"
            elif ext in [".txt", ".md"]:
                file_type = "text"
            else:
                file_type = "binary"
        else:
            file_type = "unknown"

        # Get the file's color
        color = file_colors.get(file_type, "")

        # Print the file
        print(f"{color}{icon} {file}")

    print()
