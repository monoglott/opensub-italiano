#!/usr/bin/python3

import sys

input_ = open('counted.csv')
wordict = dict([])

# Load dictionary.
for line in input_:
    [word, freq] = line.split(',')
    wordict[word] = freq.strip()

input2 = open(sys.argv[1])

for line in input2:
    word = line.strip()
    if word in wordict:
        out_str = "{:s},{:s}".format(word, wordict[word])
        print(out_str)
