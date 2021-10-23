#!/usr/bin/python3

import sys

input_ = open(sys.argv[1])

for line in input_:
    print(line.split(',')[0])


