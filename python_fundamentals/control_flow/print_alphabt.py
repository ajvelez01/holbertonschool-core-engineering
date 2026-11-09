#!/usr/bin/env python3
letters = ""
for c in "abcdefghijklmnopqrstuvwxyz":
    if c != "q" and c != "e":
        letters += c
print("{}".format(letters), end="")
