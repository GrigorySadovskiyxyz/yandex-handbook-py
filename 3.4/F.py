from itertools import product

n = int(input())
x = [i for i in range(1, n + 1)]
for index, i in enumerate(product(x, x), 1):
    print(i[0] * i[1], end=' ')
    if index % n == 0:
        print()
