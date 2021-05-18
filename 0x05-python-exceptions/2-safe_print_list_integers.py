 #!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    ctr = 0
    for n in range(0, x):
        try:
            print("{:d}".format(my_list[n]), end="")
            ctr += 1
        except (ValueError, TypeError):
            pass
    print()
    return (ctr)
