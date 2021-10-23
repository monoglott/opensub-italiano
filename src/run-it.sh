#!/bin/sh
rm -f split split-lines.txt filtered.txt counted.csv counted-final.csv
rm -f spell-checked.txt
clang++ -Wall -o split split.cpp
./split it.txt > split-lines.txt
./filter.sh split-lines.txt > filtered.txt
./counter.py filtered.txt > counted.csv
hunspell -i utf-8 -d it_IT -G counted.csv > spell-checked.txt
./matcher.py spell-checked.txt > counted-final.csv
