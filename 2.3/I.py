f = int(input())
counter = f
total = 1
while (counter != 0):
    if f == 0:
        print(total)
        break
    else:
        total *= counter
        counter = counter - 1
print(total)
