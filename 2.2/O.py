n = input()
m = input()

nmax = max(int(n[0]), int(n[1]), int(m[0]), int(m[1]))
nmin = min(int(n[0]), int(n[1]), int(m[0]), int(m[1]))

sum_all = sum([int(x) for x in [*n, *m]]) - nmax - nmin

if len(str(sum_all)) > 1:
    sum_all = str(sum_all)[1]
else:
    sum_all = sum_all

print(f'{nmax}{sum_all}{nmin}')
