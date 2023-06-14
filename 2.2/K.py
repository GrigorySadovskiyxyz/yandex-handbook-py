n = input()

min_n = min(int(n[0]), int(n[1]), int(n[2]))
max_n = max(int(n[0]), int(n[1]), int(n[2]))
mid_n = min(max(int(n[0]), int(n[1])), max(int(n[1]), int(n[2])))

if min_n + max_n == mid_n * 2:
    print('YES')
else:
    print('NO')
