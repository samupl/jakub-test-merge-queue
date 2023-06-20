import sys


# Some example comment 2
def pprint(msg, out=sys.stdout):
    out.write(msg)


def main():
    pprint('Hello world!\n')
    return True


if __name__ == '__main__':
    # test Adding a new change for demo for vincent
    main()
