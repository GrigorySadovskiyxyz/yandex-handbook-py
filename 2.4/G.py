n = int(input())
count = 3
k = count
for i in range(1, n + 1):
    for j in range(count):
        print(f'До старта {k} секунд(ы)')
        k -= 1
    print(f'Старт {i}!!!')
    count += 1
    k = count
