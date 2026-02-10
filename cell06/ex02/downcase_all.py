#!/usr/bin/env python3

import sys
def downcase_all(letters):
    return [letter.lower() for letter in letters]

if len(sys.argv) <= 1:
    print("none")
else:
    letter = sys.argv[1:]
    count = len(sys.argv[1:])
    for x in range(0,count):
        lowercased = downcase_all(letter)
        print(lowercased[x])