lll = int(input())
n = int(input())
result = []

while n != 0:
    s = input()
    result.append(s.rstrip())
    n -= 1

for o in result:
    if lll - 3 >= len(o):
        print(o[:lll])
        lll -= len(o)
    elif lll - 3 <= len(o):
        print(o[:lll - 3] + '...')
        break
