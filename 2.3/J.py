d = input()
x = 0
y = 0
while d != 'СТОП':
    v = int(input())
    if d == 'СЕВЕР':
        y += v
    elif d == 'ЮГ':
        y -= v
    elif d == 'ЗАПАД':
        x -= v
    elif d == 'ВОСТОК':
        x += v
    d = input()
print(y, x, sep="\n")
