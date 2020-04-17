import os

from Tools.Uml.FilesCollector import FilesCollector

source_dir = os.path.dirname(os.path.realpath(__file__))
collector = FilesCollector([".py"], os.path.dirname(os.path.realpath(__file__)))

for file_path in collector.get_files_by_extension(".py"):
    rel_path = os.path.relpath(os.path.dirname(file_path), source_dir)
    rel_path = os.path.join(rel_path, file_path.split("/")[-1])
    rel_path = rel_path.replace("/", "_").replace(".", "_")

    command = f"pyreverse -a 100 -s 100 -f ALL -p {rel_path} -o png {file_path}"
    print(command)
    os.system(command)
