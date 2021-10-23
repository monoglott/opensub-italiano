#!/usr/bin/python3

import sys

input_ = open(sys.argv[1])
wcount = dict([])
total = 0

for line in input_:
    total += 1
    word = line.strip().lower()
    #word = line.strip()
    if not word in wcount:
        wcount[word] = 1     # put word in dictionary
    else:
        wcount[word] += 1    # add to word count

wcount_s = sorted(wcount.items(), key=lambda x: x[1])
wcount_s.reverse()

#print("total words: " + str(total))

for item in wcount_s:
    out_str = "{:s},{:s}".format(item[0], str(item[1]))
    print(out_str)
