n = int(input())
s = dict()
total = 0
while n != 0:
    name = input()
    if name not in s:
        s[name] = 1
    else:
        s[name] += 1
    n -= 1
for value in s.values():
    if int(value) > 1:
        total += int(value)
print(total)
