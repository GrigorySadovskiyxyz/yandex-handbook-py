from sys import stdin

lines = []
for line in stdin:
    line = line.rstrip('\n').split(' ')
    for char in line:
        if isinstance(int(char), int):
            lines.append(int(char))
print(sum(lines))
