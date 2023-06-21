n = int(input())
v = set()
while n != 0:
    s = set(input().split(' '))
    v.update(s)
    n -= 1
for item in v:
    print(item)
