animals = {}
while (n := input()) != '':
    n = n.split()
    for one in n:
        if one not in animals:
            animals[one] = 1
        else:
            animals[one] += 1
for animal in animals:
    print(f'{animal} {animals[animal]}')
