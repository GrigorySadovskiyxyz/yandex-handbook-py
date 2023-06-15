n = int(input())
count = 0

while (n != 0):
    i = input()
    if i.find('зайка') != -1:
        count += 1
    n -= 1
print(count)
