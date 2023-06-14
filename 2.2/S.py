x = float(input())
y = float(input())
r = 10

# pi = 3.14 
# area = pi * 10 * 10
# parabola = pow((x * 0.5 + 0.5), 2)) - 9
# quater_circle = pi * 5 * 5 / 4
# triangle
# h_square = (x * x) + (y * y)
# h = sqrt(h_square)


if x ** 2 + y ** 2 > r ** 2:
    print('Вы вышли в море и рискуете быть съеденным акулой!')   
elif x >= 0 and y >= 0 and (x ** 2 + y ** 2) <= 25:
    print('Опасность! Покиньте зону как можно скорее!')
elif (x - 5) * (x + 7) <= 4 * y and y < 0:
    

