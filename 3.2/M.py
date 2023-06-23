n = int(input())
all_dishes = list()

for i in range(n):
    value = input()
    all_dishes.append(value)

m = int(input())
for j in range(m):
    count = int(input())
    for each in range(count):
        done = input()
        if done in all_dishes:
            del all_dishes[all_dishes.index(done)]

if len(all_dishes) == 0:
    print('Готовить нечего')
else:
    for one in sorted(all_dishes):
        print(one)
