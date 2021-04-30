#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    num_args = len(argv) - 1
    if num_args is 0:
        print("{:d} arguments.".format(num_args))
    elif num_args is 1:
        print("{:d} argument:".format(num_args))
    else:
        print("{:d} arguments:".format(num_args))

    for n in range(1, len(argv)):
        print("{:d}: {:s}".format(n, argv[n]))
