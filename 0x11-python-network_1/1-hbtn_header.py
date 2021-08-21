#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL and displays
the value of the X-Request-Id variable found in the header of the response.
"""

from sys import argv
from urllib import request

if __name__ == "__main__":
    url = argv[1]
    req = request.urlopen(url)
    with req as response:
        """
        hdr = response.info()['X-Request-Id']
        print(hdr)
        """
        out = response.getheader('X-Request-Id')
        print(out)
