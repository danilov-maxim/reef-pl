import csv
import sys


with open('input.csv', 'r') as read_file:

    data = list(csv.reader(read_file, delimiter=','))

writer = csv.writer(sys.stdout)
for line in data:
    if len(line) > 2:
        line = [line[0], line[2], line[1], *line[3:]]
    print(','.join(str(bit) for bit in line))

import csv
import sys


read_file = sys.stdin.readlines()
data = list(csv.reader(read_file, delimiter=','))

writer = csv.writer(sys.stdout)
for line in data:
    if len(line) > 2:
        line = [line[0], line[2], line[1], *line[3:]]
    writer.writerow(line)