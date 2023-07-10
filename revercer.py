# in Stdin is a lines. reverse the lines input and symbols in lines.
# in such a way that "abs\ndef" transforms to "fed\nsba" and write it to stdout.

import sys

for line in [line[::-1] for line in sys.stdin.readlines()][::-1]:
    sys.stdout.write(line)
