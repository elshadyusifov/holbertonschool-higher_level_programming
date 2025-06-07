#!/usr/bin/python3
import json
'''create JSON string'''


def to_json_string(my_obj):
    '''module JSON string'''
    json_string = json.dumps(my_obj)
    return json_string
