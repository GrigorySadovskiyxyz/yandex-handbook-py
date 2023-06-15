total = 0
while (price := float(input())) != 0:
    if price >= 500:
        price = price - (0.1 * price)
        total += price
    else:
        total += price
print(total)
