from itertools import chain

items = [[x for x in input().split(', ')] for i in range(3)]
list_flat = sorted(list(chain.from_iterable(items)))
for index, value in enumerate(list_flat, 1):
    print(f'{index}. {value}')
