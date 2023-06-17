n = int(input())
counter = 0
while n != 0:
    s = input()
    counter += s.count('зайка')
    n -= 1
print(counter)
