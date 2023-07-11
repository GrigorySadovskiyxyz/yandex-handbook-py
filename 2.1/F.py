item_name = input()
item_price = input()
item_weight = input()
stock = input()
total_price = (int(item_price) * int(item_weight))
change = int(stock) - total_price
print("Чек")
print(item_name, f"{item_weight}кг", f"{item_price}руб/кг", sep=" - ")
print("Итого:", f"{total_price}руб")
print("Внесено:", f"{stock}руб")
print("Сдача:", f"{change}руб")

