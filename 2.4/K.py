all = []
n = int(input())
while n != 0:
    s = input()
    all.append(s)
    n -= 1
key = input().lower()
for one in all:
    if one.lower().find(key) != -1:
        print(one)
    else:
        continue
