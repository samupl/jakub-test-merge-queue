import sys


def pprint(msg, out=sys.stdout):
    out.write(msg)


def main():
    pprint('Hello world!\n')
    return True


if __name__ == '__main__':
    main()
