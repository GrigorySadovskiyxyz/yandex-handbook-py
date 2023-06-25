from itertools import accumulate

string = [x + ' ' for x in input().split()]
for value in accumulate(string):
    print(value)

