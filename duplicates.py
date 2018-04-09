import os
import sys
from collections import defaultdict


def get_size(filepath):
    return os.stat(filepath)[6]


def get_files_data(root_dir):
    files = defaultdict(list)
    for dirpath, dirnames, filenames in os.walk(root_dir):
        try:
            for filename in filenames:
                fullpath = os.path.join(dirpath, filename)
                file_stat = (filename, (get_size(fullpath)))
                files[file_stat].append(fullpath)
        except (FileNotFoundError, PermissionError):
            pass
    return files


def get_duplicates(files_data):
    return {k: v for k, v in files_data.items() if len(v) > 1}


def prettify_data(files_data):
    for k, v in files_data.items():
        print('File:', k[0], ' Size:', k[1], ' Files:', v)


if __name__ == '__main__':

    if len(sys.argv) != 2:
        sys.exit('Вы не указали путь')
    root_path = sys.argv[1]

    files_data = get_files_data(root_path)
    duplicates = get_duplicates(files_data)
    prettify_data(duplicates)
