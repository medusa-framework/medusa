import os

for module in os.listdir(os.path.dirname(__file__)):
    if (
        "__init__" in module or
        "__pycache__" in module or
        ".gitignore" in module
    ):
        continue
    module.replace(".py", "")
    exec(f"from . import {module}")
