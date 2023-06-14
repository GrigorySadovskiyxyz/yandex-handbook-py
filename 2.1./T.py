n = int(input())
m = int(input())
k1 = int(input())
k2 = int(input())
total = n * m
x = (total - k2 * n) / (k1 - k2)
y = n - x
print(int(x), int(y))
