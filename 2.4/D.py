n = int(input())
counter = 0
sum = 0
while counter != n:
    number = input()
    for i in number:
        sum += int(i)
    counter += 1
print(sum)
