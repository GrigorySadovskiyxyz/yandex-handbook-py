import copy
n = input().lower().replace(" ", "")
n = list(n)
n_copy = copy.deepcopy(n)
n = n[::-1]
if ''.join(n) == ''.join(n_copy):
    print('YES')
else:
    print('NO')
