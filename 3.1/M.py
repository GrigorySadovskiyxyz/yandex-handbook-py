n = int(input())
values = []
result = []
while n != 0:
    v = int(input())
    values.append(v)
    n -= 1
deg = int(input())
for val in values:
    result.append(val ** deg)
for res in result:
    print(res)
