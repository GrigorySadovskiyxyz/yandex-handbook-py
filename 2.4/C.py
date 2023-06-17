n = int(input())
k = 1
w = 1
while k <= n:
    for i in range(k, k + w):
        if i <= n:
            print(i, end=" ")
    k += w 
    w += 1
    print()
