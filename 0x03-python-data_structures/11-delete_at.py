#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    if 0 <= idx < len(my_list):
        del(my_list[idx])
    return (my_list)
# This is a single-line comment in Python
