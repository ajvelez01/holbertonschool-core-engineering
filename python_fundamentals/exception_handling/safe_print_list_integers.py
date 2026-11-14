#!/usr/bin/env python3
def safe_print_list_integers(my_list=[], x=0):
    printed = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            printed += 1
        except IndexError:
            print("", end="", flush=True)
            raise
        except (ValueError, TypeError):
            continue
    print()
    return printed
