# Virginia Link
# CS 362
# HW4 program to create a full name from a given first and last
# 02/07/2021

def full(first, last):
    if not isinstance(first, str) or not isinstance(last, str): 
        print("Oops! A name has to be a string!")
        return 0 
    return first+' '+last


