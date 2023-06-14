n = int(input())
m = int(input())

p = 7
v = 6

p -= 3
v += 3
p += 2
v += 5
v -= 2
p += n
v += m

if p > v:
    print('Петя')
else:
    print('Вася')
