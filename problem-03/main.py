#!/usr/bin/python3

"""
See the README.md for instructions on how to run this file, and problem-03.md
for instructions on the problem this code solves :D
"""

from itertools import permutations
import sys
import argparse

parser = argparse.ArgumentParser(
    description='Runs the problem 3 solver against some input file'
)

parser.add_argument(
    'input_file',
    action='store',
    type=argparse.FileType('r'),
    help='the input file to create all string permutations from'
)

args = parser.parse_args()

# argparse will ensure that the CLI options are valid, and that the file exists
# and is readonly


# now iterate through ever line
for line in args.input_file:
    # print all the permutations of this line to stdout
    print(','.join(
        # make all the permutations from the line (without newlines)
        # and return them as a list of permutation strings
        ''.join(p) for p in permutations(sorted(line.rstrip('\r\n')))
    ))

# we're done here folks!
args.input_file.close()
