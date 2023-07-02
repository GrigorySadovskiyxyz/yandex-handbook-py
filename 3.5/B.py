from sys import stdin

changes = []
for line in stdin:
    line = line.rstrip('\n').split(' ')
    height_change = int(line[2]) - int(line[1])
    changes.append(height_change)
print(round(sum(changes) / len(changes)))
