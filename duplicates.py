import os
import sys
from collections import defaultdict


def get_size(filepath):
    return os.stat(filepath)[6]


def get_files(root_dir):
    files = defaultdict(int)
    for (dirpath, dirnames, filenames) in os.walk(root_dir):
        try:
            for filename in filenames:
                fullpath = os.path.join(dirpath, filename)
                file_stat = (filename, get_size(fullpath))
                files[file_stat] += 1
        except (FileNotFoundError, PermissionError):
            pass
    return files


def get_duplicates(files):
    return sorted({key: value for key, value in files.items() if value > 1})


if __name__ == '__main__':

    if len(sys.argv) != 2:
        sys.exit('Вы не указали путь')
    root_path = sys.argv[1]

    files_data = get_files(root_path)
    duplicates = get_duplicates(files_data)
    print(duplicates)
