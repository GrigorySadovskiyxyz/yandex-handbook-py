from math import gcd
n = gcd(*[int(x) for x in input().split()])
print(n)
