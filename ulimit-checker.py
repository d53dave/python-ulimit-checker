import fd

check_fns = [fd.run_fd_check]

if __name__ == "__main__":
    print('Starting ulimit test suite with fns:',
          list(map(lambda fn: fn.__name__, check_fns)))
    for fn in check_fns:
        fn()
    print('Test suite finished.')
