n = int(input())
result = {}
counter = 0
for i in range(n):
    value = input()
    result[value] = 1 + result.get(value, 0)

for count in sorted(result):
    if result[count] > 1:
        print(f'{count} - {result[count]}')
    elif result[count] == 1:
        counter += 1
if counter == n:
    print('Однофамильцев нет')
