#!/bin/python3

from collections import Counter


if __name__ == '__main__':
    s = sorted(input())
    items = Counter(s).most_common(3)

    for item in items:
        print(* item)
