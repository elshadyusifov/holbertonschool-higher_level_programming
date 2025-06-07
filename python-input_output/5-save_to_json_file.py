#!/usr/bin/python3
'''save obj to a file'''
import json


def save_to_json_file(my_obj, filename):
    '''save obj to a file'''
    with open(filename, "w", encoding="utf-8") as file:
        json.dumps(my_obj, file, ensure_ascii=False, indent=4)
        return my_obj
