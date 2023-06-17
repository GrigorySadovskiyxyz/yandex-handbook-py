n = int(input())
result = ''
for i in range(n):
    m = input()
    highest = 0
    for j in range(len(m)):
        if highest <= int(m[j]):
            highest = int(m[j])
        else:
            highest = highest
    result += str(highest)
print(int(result))
