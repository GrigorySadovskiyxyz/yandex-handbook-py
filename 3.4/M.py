from itertools import permutations

n = int(input())
arr = []
while (n != 0):
    string = input()
    arr.append(string)
    n -= 1
for item in sorted(list(permutations(arr), 3)):
    print(', '.join(item).rstrip(', '))
