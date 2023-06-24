result = {}
while (n := input().strip()) != '':
    f1, f2 = n.split()
    if f1 in result.keys():
        result[f1].append(f2)
    else:
        result[f1] = [f2]
    if f2 in result.keys():
        result[f2].append(f1)
    else:
        result[f2] = [f1]
print(result)
