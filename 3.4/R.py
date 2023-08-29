from itertools import product

items = [0, 1]
istrue = input()
print('a b c f')

for item in product(items, repeat=3):
    a = item[0]
    b = item[1]
    c = item[2]
    f = int(eval(istrue))
    print(a, b, c, f)
