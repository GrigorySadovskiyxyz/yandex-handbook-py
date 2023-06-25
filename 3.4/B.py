first = input().split(', ')
second = input().split(', ')
if len(first) > len(second):
    for i in range(len(first) - 1):
        print(f'{first[i]} - {second[i]}')
elif len(second) > len(first):
    for i in range(len(second) - 1):
        print(f'{first[i]} - {second[i]}')
else:
    for i in range(len(second)):
        print(f'{first[i]} - {second[i]}')

