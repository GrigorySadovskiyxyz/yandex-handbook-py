p = int(input())
v = int(input())
t = int(input())
if p < t < v:
    print('Вася')
elif v < t < p:
    print('Петя')
elif v < p < t:
    print('Толя')

