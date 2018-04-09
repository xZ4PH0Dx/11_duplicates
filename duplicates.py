import os
import sys
from collections import defaultdict


def get_size(filepath):
    return os.stat(filepath).st_size


def get_files_info(root_dir):
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


def get_duplicates(files_info):
    return {file_size: file_locations
            for file_size, file_locations
            in files_data.items() if len(file_locations) > 1}


def prettify_data(files_info):
    for file_size, file_locations in files_info.items():
        print('\n Filename:', file_size[0],
              ' Size:', file_size[1], '\n',
              'Found ', len(file_locations),
              ' Duplicate Files:\n\t',
              ('\n\t'.join(file_locations))
              )


if __name__ == '__main__':

    if len(sys.argv) != 2:
        sys.exit('Вы не указали путь')
    root_path = sys.argv[1]

    files_data = get_files_info(root_path)
    duplicates = get_duplicates(files_data)
    prettify_data(duplicates)
