n = int(input())
result = list()
need = list()
for i in range(n):
    secondname_type = input()
    if secondname_type not in result:
        result.append(secondname_type)
poridge = input()
for i in result:
    i = i.split(' ')
    if poridge in i:
        need.append(i)

if len(need) == 0:
    print('Таких нет')
else:
    need = sorted(need)
    for one in need:
        print(one)
