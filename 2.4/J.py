all_char = []
d = {}
while (n := input().upper()) != "ФИНИШ":
    n = n.lower().replace(" ", "")
    all_char = [*all_char, *n]
letters = set()
for i in all_char:
    letters.add(i)
for let in letters:
    d[let] = all_char.count(let)
sorted_values = str(max(sorted(d.values())))
sorted_dict = {}
for k in d.keys():
    if d[k] == int(sorted_values):
        sorted_dict[k] = d[k]
sorted_dict = sorted([*sorted_dict.keys()])[0]
print(sorted_dict)

