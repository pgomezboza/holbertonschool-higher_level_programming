#!/usr/bin/python3
"""
Python script that takes in a URL and an email,
sends a POST request to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)
"""

from sys import argv
from urllib import request
from urllib import parse

if __name__ == "__main__":
    url = argv[1]
    values = {'email': argv[2]}

    params = parse.urlencode(values)
    enc_data = params.encode('utf-8')
    req1 = request.Request(url, enc_data)
    req2 = request.urlopen(req1)
    with req2 as response:
        dcd_data = response.read().decode('utf-8')
        out = dcd_data
        print(out)
