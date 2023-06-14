p = int(input())
v = int(input())
t = int(input())

if p > v and p > t:
    first = 'Петя'
    if v > t:
        second = 'Вася'
        third = 'Толя'
    elif t > v:
        second = 'Толя'
        third = 'Вася'
if t > v and t > p:
    first = 'Толя'
    if v > p:
        second = 'Вася'
        third = 'Петя'
    elif p > v:
        second = 'Петя'
        third = 'Вася'
if v > t and v > p:
    first = 'Вася'
    if t > p:
        second = 'Толя'
        third = 'Петя'
    elif p > t:
        second = 'Петя'
        third = 'Толя'

print(f"1. {first}")
print(f"2. {second}")
print(f"3. {third}")
