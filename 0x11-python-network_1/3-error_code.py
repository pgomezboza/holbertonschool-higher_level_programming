#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL
and displays the body of the response (decoded in utf-8).
"""

from sys import argv
from urllib import request
from urllib import error

if __name__ == "__main__":
    url = argv[1]
    req1 = request.Request(url)
    try:
        req2 = request.urlopen(req1)
        with req2 as response:
            print(response.read().decode('utf-8'))
    except error.HTTPError as err:
        print("Error code: {}".format(err.code))
