#!/usr/bin/python3

def read_file(filename=""):
    with open("my_file_0.txt", "r", encoding="UTF8") as myfile:
    print(myfile.read())
