#!/usr/bin/python3
for n in range(97, 123):
    if chr(n) is not 'e' and chr(n) is not 'q':
        print('{}'.format(chr(n)), end='')
