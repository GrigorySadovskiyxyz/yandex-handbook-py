from itertools import product

n = int(input())
print('А Б В')
x = product(range(1, n + 1), range(1, n + 1), range(1, n + 1))
for i in x:
    if sum(i) == n:
        print(i[0], i[1], i[2])
