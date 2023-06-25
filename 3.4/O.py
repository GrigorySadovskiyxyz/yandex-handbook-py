n = input().split()
result = []
for one in n:
    one = str(bin(int(one)).replace("0b", ""))
    counter = {}
    counter['digits'] = len(one)
    counter['units'] = one.count('1')
    counter['zeros'] = one.count('0')
    result.append(counter)
print(result)
