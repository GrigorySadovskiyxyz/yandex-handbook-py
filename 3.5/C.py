from sys import stdin

for line in stdin:
    if line[0] != '#':
        if '#' in line:
            print(line[:line.find('#')].rstrip())
        else:
            print(line.rstrip())


