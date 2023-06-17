n = ['Манная', 'Гречневая', 'Пшённая', 'Овсяная', 'Рисовая']
count = int(input())
f1 = count // len(n)
f2 = count % len(n)
n = n * f1 + n[0:f2]
for one in n:
    print(one)

