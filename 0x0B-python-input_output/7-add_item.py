#!/usr/bin/python3
"""
Module: 7-add_item
"""
import json
import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

my_file = "add_item.json"

try:
    my_list = load_from_json_file(my_file)
except:
    my_list = []

my_list = my_list + sys.argv[1:]
save_to_json_file(my_list, my_file)
