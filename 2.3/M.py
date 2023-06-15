n = int(input())
lowest = []

while (n != 0):
    i = input()
    lowest.append(i)
    n -= 1

low = sorted(lowest)[0]
print(low)
