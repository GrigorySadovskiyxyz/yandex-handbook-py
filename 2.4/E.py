n = int(input())
stop = 'ВСЁ'
result = 0
for i in range(n):
    value = input()
    k = i
    while value != stop:
        if value == 'зайка' and k == i:
            result += 1
            k = -1
        value = input()
print(result)

