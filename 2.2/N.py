n = input()

first = int(n[0])
second = int(n[1])
third = int(n[2])

max = None
average = None
lowest = None

if first >= second and first >= third:
    max = first
    if second >= third:
        average = second
        lowest = third
    else:
        average = third
        lowest = second
if second >= first and second >= third:
    max = second
    if third >= first:
        average = third
        lowest = first
    else:
        average = first
        lowest = third
if third >= first and third >= second:
    max = third
    if second >= first:
        average = second
        lowest = first
    else:
        average = first
        lowest = second


if lowest == 0 and average == 0:
    print(f"{max}{lowest} {max}{average}")
elif lowest == 0 and average == max:
    print(f"{max}{lowest} {max}{average}")
elif lowest != 0 and average == lowest and average != max:
    print(f"{average}{lowest} {max}{average}")
elif lowest != 0 and average == max and lowest != max:
    print(f"{lowest}{average} {max}{average}")
elif lowest != average and average != max and lowest != 0:
    print(f"{lowest}{average} {max}{average}")
elif lowest != average and average != max and lowest == 0:
    print(f"{average}{lowest} {max}{average}")
elif lowest == average and average == lowest:
    print(f"{average}{lowest} {max}{average}")
