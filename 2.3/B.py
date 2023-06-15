counter = 0
while (name := input()) != "Приехали!":
    if 'зайка' in name:
        counter += 1
print(counter)
