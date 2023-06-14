a = float(input())
b = float(input())
c = float(input())

d = (b * b) - (4 * a * c)

if d < 0 and a > 0 and c > 0:
    print('No solution')
elif int(a) == 0 and int(c) == 0 and int(b) == 0:
    print('Infinite solutions')
elif d == 0:
    x = -b / (2 * a)
    print("{:.2f}".format(x))
elif d > 0:
    x1 = (-b + ((b * b) - 4 * a * c) ** 0.5) / (2 * a)
    x2 = (-b - ((b * b) - 4 * a * c) ** 0.5) / (2 * a)
    print("{:.2f}".format(x2), "{:.2f}".format(x1))
