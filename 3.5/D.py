from sys import stdin

data = [line.strip() for line in stdin]
search_word = data[len(data) - 1]
data = data[0:len(data) - 1]

for item in data:
    if item.lower().find(search_word.lower()) != -1:
        print(item)
    elif item.lower().find(search_word.lower()) < 0:
        continue
