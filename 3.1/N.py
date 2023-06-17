n = input().split(' ')
deg = int(input())
result = []
for val in n:
    result.append(str(int(val) ** deg))
print(' '.join(result))
