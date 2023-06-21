n = int(input())
while n != 0:
    s = input()
    if s.find('зайка') != -1:
        print(s.find('зайка') + 1)
    else:
        print('Заек нет =(')
    n -= 1
