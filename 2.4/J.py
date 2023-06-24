orange = int(input())
res = [(i, j, orange - i - j)
       for i in range(1, orange-1) 
       for j in range(1, orange-i)]
for i in res:
    print(*i)
