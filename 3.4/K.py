from itertools import product, starmap

n = int(input())
m = int(input())
counter = 0
for i in range(1, n + 1):
    print(*starmap(lambda x, y: str(x + y).rjust(len(str(n * m))), product([counter], range(1, m + 1))))
    counter += m
