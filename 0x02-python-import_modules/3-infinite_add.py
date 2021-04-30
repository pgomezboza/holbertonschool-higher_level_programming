#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    add = 0
    for n in range(1, len(argv)):
        add = add + int(n)
    print("{:d}".format(add))
