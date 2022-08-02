#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#


def plusMinus(arr):

    pos = neg = zer = 0
    n = len(arr)
    for i in arr:
        if(i > 0):
            pos = pos + 1
        if(i < 0):
            neg = neg + 1
        if (i == 0):
            zer = zer + 1
    print(pos / n)
    print(neg / n)
    print(zer / n)


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
