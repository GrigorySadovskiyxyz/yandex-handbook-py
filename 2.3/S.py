#import math
#import random
#
#n = random.randint(1, 1000)
#
#while(value := int(input()) != n):
#    if n > value:
#        n = n + math.ceil(value / 2)
#        print('Больше')
#    elif n < value:
#        n = math.ceil(value / 2)
#        print('Меньше')
#    elif n == value:
#        print('Угадал!')
#        break


a1 = 1
a2 = 1000
b = ''
d = 0
c = d

while b != 'Угадал!':
    c = (a1 + a2) // 2
    if c == d:
        c == c - 1
    print(c)
    b = input()
    if b == 'Больше':
        a1 = c
    elif b == 'Меньше':
        a2 = c
d = c
