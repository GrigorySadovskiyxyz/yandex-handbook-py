n = input()
m = input()
w = input()

i = [n, m, w]
result = []

for one in i:
    if one.find('зайка') > 0:
        result.append(one)

print(f'{sorted(result)[0]} {len(sorted(result)[0])}')
