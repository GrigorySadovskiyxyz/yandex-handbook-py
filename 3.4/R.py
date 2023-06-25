n = int(input())
counter = 0
coordinates = []
while n != 0:
    xi_yi = input().split()
    coordinates.append(*xi_yi)
    n -= 1
print(coordinates)
