n = input()
counter = 0
d = []
for x in range(len(n) - 1):
    if n[x] != n[x + 1]:
        counter += 1
        d.append(f'{n[x]} {counter}')
        counter = 0
    else:
        counter += 1
d.append(f'{n[-1]} {counter + 1}')
for i in d:
    print(i)

