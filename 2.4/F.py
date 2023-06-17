import math

n = int(input())
result = []
while (n != 0):
    i = int(input())
    result.append(i)
    n -= 1

print(math.gcd(*result))
