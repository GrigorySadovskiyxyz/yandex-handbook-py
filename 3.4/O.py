from itertools import permutations

n = int(input())
res = []
while (n != 0):
    string = input().rstrip().split(', ')
    res.append(string)
    n -= 1

res = [item for row in res for item in row]
for item in permutations(sorted(res), 3):
    print(' '.join(item))

