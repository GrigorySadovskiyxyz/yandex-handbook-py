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
        counter -= 1
print(counter if counter > 0 else "Таких нет")
