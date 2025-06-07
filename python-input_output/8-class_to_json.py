#!/usr/bin/python3
'''class to json'''
import json


def class_to_json(obj):
    json_string = json.dumps(obj)
    return json_string
