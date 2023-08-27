n = int(input())
arr = []
while (n != 0):
    string = input().split(', ')
    arr.append(string)
    n -= 1
arr = sorted([item for row in arr for item in row])
for index, each in enumerate(arr):
    print(f'{index + 1}. {each}')
