#!/usr/bin/python3
'''class to json'''


def class_to_json(obj):
    json_string = json.dumps(obj.__dict__)
    return json_string
