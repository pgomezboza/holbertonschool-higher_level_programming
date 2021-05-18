#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    n = 0
    for n in range(0, x):
        try:
            print(my_list[n], end="")
            n += 1
        except:
            break
    print()
    return (n)
