import sys

from tempfile import NamedTemporaryFile
from typing import List, Any


def create_files(num_files: int) -> int:
    try:
        files: List[Any] = []
        open_file_count = 0
        with NamedTemporaryFile() as f:
            # add file to a list so that it doesn't get GC-d
            files.append(f.file)  # type: ignore
            open_file_count += 1
    except IOError as ioe:
        print('Caught', ioe)
        return open_file_count

    return num_files


def run_fd_check(**kwargs):
    num_files = int(kwargs['num_files'])
    print('Running fd check with number of files:', num_files)
    created_file_count = create_files(num_files)
    print('fd.py successfully created', created_file_count, 'files.')


if __name__ == '__main__':
    run_fd_check(num_files=sys.argv[1])
