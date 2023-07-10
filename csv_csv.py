# Swap csv columns
# Stdin is a small csv. Swap the columns in such a way that "1,2,3\nMike,Dyke,Pike" becomes "1,3,2\nMike,Pike,Dyke" and write to stdout.

# sample Input
# 1,2,3,4
# a,b,c,d
# Sample Output
# 1,3,2,4
# a,c,b,d

# Sample Input
# 1,"2,3",4
# Sample Output
# 1,4,"2,3"

import csv
import sys


with open('input.csv', 'r') as read_file:

    data = list(csv.reader(read_file, delimiter=','))

writer = csv.writer(sys.stdout)
for line in data:
    if len(line) > 2:
        line = [line[0], line[2], line[1], *line[3:]]
    # print(','.join(str(bit) for bit in line))
    writer.writerow(line)
