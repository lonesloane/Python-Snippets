#! /home/stephane/anaconda3/bin/python

import math


def area(name: str, radius: float=0) -> str:
    area = math.pi * radius ** 2
    return "The area of {} is {}".format(name, area)


print(area('Bob', 5.0))
