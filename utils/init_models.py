import importlib.util
import inspect
import logging
from pathlib import Path
import os
import sys

from config.app import db


def init_modules(modules_path):
    if os.path.isdir(modules_path):
        db_models = []
    else:
        logging.error("MODULES_PATH not valid. Exiting.")
        sys.exit(1)
    for root, dirs, files in os.walk(modules_path):
        # Ignore __pycache__ and seeders directories
        ignore_dirs = ["__pycache__", "seeders"]
        dirs[:] = [d for d in dirs if d not in ignore_dirs]
        for file in files:
            if file.startswith("__") or file.endswith(".pyc") or not file.endswith(".py"):
                continue
            # Create an absolute path to the Python file
            filepath = os.path.join(root, file)
            module_name = f"{Path(filepath).relative_to(modules_path).with_suffix('').as_posix()}"
            module_import = f"modules.{module_name}".replace("/", ".")
            module = importlib.import_module(f"{module_import}")
            # Iterate through the module's contents
            for name, obj in inspect.getmembers(module):
                if inspect.isclass(obj) and issubclass(obj, db.Model) and obj != db.Model:
                    # Instantiate the class and add it to the list of db models
                    instance = obj()
                    db_models.append(instance)
                    # TODO Add logging for what models have been registered
    return db_models
