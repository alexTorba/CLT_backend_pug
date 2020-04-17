import os

dependencies = ["requests", "psutil"]

for dependency in dependencies:
    os.system("python -m pip install {} --user".format(dependency))
