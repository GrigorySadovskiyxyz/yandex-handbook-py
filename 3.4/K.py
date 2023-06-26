from itertools import product

n = int(input())
m = int(input())
counter = 0
for i in range(1, n + 1):
    print(*product([counter], range(1, m + 1)))
    counter += m
print(x)
