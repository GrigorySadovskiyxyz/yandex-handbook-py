n = input()
total = 0
counter = len(n) - 1
while (counter != -1):
    total += int(n[counter])
    counter -= 1
print(total)
    
