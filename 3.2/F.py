n = int(input())
m = int(input())
result = list()
counter = 0
for i in range(n + m):
    secondname = input()
    if secondname not in result:
        result.append(secondname)
        counter += 1
    else:
        del result[result.index(secondname)]
        counter -= 1
if counter == 0:
    print('Таких нет')
else:
    result = sorted(result)
    for i in result:
        print(i)
