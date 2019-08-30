import fd
import os

from typing import Dict, Any

check_fns = [fd.run_fd_check]


def get_opts_from_env() -> Dict[str, Any]:
    return {
        'num_files': os.getenv('NUM_FILES', 10000),
    }


if __name__ == "__main__":
    print('Starting ulimit test suite')

    opts = get_opts_from_env()

    for fn in check_fns:
        print('Running', fn.__name__)
        fn(**opts)

    print('Test suite finished.')
