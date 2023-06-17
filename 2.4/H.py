n = int(input())
answer = ''
comp = 0
result = None
for i in range(n):
    name = input()
    value = input()
    sum = 0
    for j in value:
        sum += int(j)
    answer += f'{name} {sum} '
answer = answer.split(' ')
for n in range(1, len(answer), 2):
    if comp <= int(answer[n]):
        comp = int(answer[n])
        result = answer[n - 1]
    elif comp >= int(answer[n]):
        result = result
print(result)
