import os
import re

PROJECT_DIR = os.path.abspath(os.getcwd())


def load_confs():
    # Find all .conf files in the directory and its subdirectories
    conf_files = []
    for root, dirs, files in os.walk(PROJECT_DIR):
        for file in files:
            if file.endswith('.conf'):
                conf_files.append(os.path.join(root, file))

    # Load variables from medusa.conf first, then from other conf files
    conf_files.sort(key=lambda x: 0 if 'medusa.conf' in x else 1)

    # Process each conf file
    for conf_file in conf_files:
        with open(conf_file, 'r') as f:
            for line in f:
                # Ignore comments and empty lines
                if line.startswith('#') or line.strip() == '':
                    continue
                line = line.split("=")
                line[1] = line[1].strip()
                line[1] = line[1].replace('"', "")
                line[1] = line[1].replace("'", "")
                os.environ[line[0]] = line[1]
