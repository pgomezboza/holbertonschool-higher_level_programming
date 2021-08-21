#!/usr/bin/python3
"""
Python script that fetches https://intranet.hbtn.io/status
"""

import urllib.request

if __name__ == "__main__":
    url = 'https://intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as resp:
        website = resp.read()
        print('Body response:')
        print("\t- type: {}".format(type(website)))
        print("\t- content: {}".format(website))
        print("\t- utf8 content: {}".format(website.decode('utf-8')))
