a = int(input())
b = int(input())
c = int(input())

if a >= b and a >= c:
    sum = b ** 2 + c ** 2
    if a ** 2 == sum:
        print('100%')
    elif a ** 2 > sum:
        print('велика')
    elif a ** 2 < sum:
        print('крайне мала')
elif b >= a and b >= c:
    sum = a ** 2 + c ** 2
    if b ** 2 == sum:
        print('100%')
    elif b ** 2 > sum:
        print('велика')
    elif b ** 2 < sum:
        print('крайне мала')
elif c >= a and c >= b:
    sum = b ** 2 + a ** 2
    if c ** 2 == sum:
        print('100%')
    elif c ** 2 > sum:
        print('велика')
    elif c ** 2 < sum:
        print('крайне мала')
    
