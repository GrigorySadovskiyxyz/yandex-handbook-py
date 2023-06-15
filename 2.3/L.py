n = input()
counter = len(n) - 1
highest = int(n[counter])
while (counter != -1):
    if highest <= int(n[counter - 1]):
        highest = int(n[counter - 1])
    counter -= 1
print(highest)

