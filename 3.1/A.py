n = int(input())
temp = False
for i in range(n):
    word = input()
    if word[0] == 'а' or word[0] == 'б' or word[0] == 'в':
        temp = True
    else:
        temp = False
        break
if temp:
    print('YES')
else:
    print('NO')
