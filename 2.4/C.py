lol = int(input())
n = int(input())
for i in range(n):
    w = input()
    if len(w) <= lol:
        print(w)
    elif len(w) >= lol:
        print(w[0:lol - 3] + '...')
