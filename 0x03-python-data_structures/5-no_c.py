def no_c(my_string):
    new_string = ""
    for n in my_string:
        if n is not 'c' and n is not 'C':
            new_string += n
    return (new_string)
