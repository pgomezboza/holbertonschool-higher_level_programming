#!/usr/bin/python3

# search_replace - function that replaces all occurrences
# of an element by another in a new list.

# @my_list: initial list
# @search: element to replace
# @replace: new element
#
# Return: new list
def search_replace(my_list, search, replace):
    new_list = []
    for n in my_list:
        if(n == search):
            new_list.append(replace)
        else:
            new_list.append(n)
    return (new_list)
