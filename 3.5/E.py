from sys import stdin

data = [line.strip() for line in stdin]
value = []

for item in data:
    item = item.split()
    for each in item:
        if each.lower() == each[::-1].lower():
            value.append(each)

value = set(value)

for one in sorted(value):
    print(one)

