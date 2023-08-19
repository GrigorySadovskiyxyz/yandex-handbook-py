from math import gcd
import sys

for line in sys.stdin:
    nums = line.strip('\n').split()
    nums = list(map(int, nums))
    print(gcd(*nums))
