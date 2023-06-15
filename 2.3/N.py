num = int(input())
 
if num == 1:
    print('NO')
elif num > 1:
    for i in range(2, int(num / 2) + 1):
        if (num % i) == 0:
            print('NO')
            break
    else:
        print('YES')
else:
    print('NO')
