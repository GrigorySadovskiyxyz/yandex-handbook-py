result = []
while (n := input().strip()) != '':
    n = n.split()
    for index, value in enumerate(n):
        if value == 'зайка':
            if index == 0:
                result.append(n[index + 1])
            elif index == len(n) - 1:
                result.append(n[index - 1])
            else:
                result.append(n[index + 1])
                result.append(n[index - 1])
result = set(result)
for each in result:
    print(each)
