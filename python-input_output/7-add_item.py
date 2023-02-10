#!/usr/bin/python3
""" Load, add, save """
import sys
import json


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

if __name__ == '__main__':
    args = sys.argv
    filename = "add_item.json"

    with open(filename, 'a+', encoding="utf-8") as f:
        try:
            items = load_from_json_file(filename)
        except:
            items = []
        items.extend(args[1:])
        save_to_json_file(items, filename)