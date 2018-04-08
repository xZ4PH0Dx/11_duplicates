import os
import sys


def get_size(filepath):
    return os.stat(filepath)[6]


def get_doubles(root_dir):
    files = []
    doubles = []
    for (dirpath, dirnames, filenames) in os.walk(root_dir):
        try:
            for filename in filenames:
                fullpath = os.path.join(dirpath, filename)
                file_stat = [filename, get_size(fullpath)]
                if file_stat in files:
                    if file_stat not in doubles:
                        doubles.append(file_stat)
                else:
                    files.append(file_stat)
        except (PermissionError, FileNotFoundError):
            pass
    return sorted(doubles)


if __name__ == '__main__':

    if len(sys.argv) != 2:
        sys.exit('Вы не указали путь')
    root_path = sys.argv[1]

    print(get_doubles(root_path))
