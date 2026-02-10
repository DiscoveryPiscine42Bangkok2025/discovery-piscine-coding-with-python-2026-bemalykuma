#!/usr/bin/env python3

import sys
if len(sys.argv) <= 1:
    print("none")
else:
    letters = sys.argv[1:]
    for letter in letters:
        eight_digit = slice(0,8)
        if len(letter) >= 8:
            print(letter[eight_digit])
        else:
            count = len(letter)
            number = 8 - count
            print(f"{letter}{'Z' * number}")