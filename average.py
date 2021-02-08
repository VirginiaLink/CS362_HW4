# Virginia Link
# CS 362
# HW4 program to calculate the average of the elements in an array
# 02/07/2021


def calc(array):
    if not array:
        print("Oops! This array doesn't have any values in it!")
        return 0
    for x in array:
        if not isinstance(x, float):
            print("Oops! This array has non numerical values!")
            return 0
       
    temp = 0
    for i in range(len(array)):
        temp = temp + array[i]
    return temp/len(array)


