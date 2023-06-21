n = int(input())
m = int(input())
mannaya_kasha = set()
ovsianaya_kasha = set()
while n != 0:
    s = input()
    mannaya_kasha.add(s)
    n -= 1
while m != 0:
    s = input()
    ovsianaya_kasha.add(s)
    m -= 1
diff = mannaya_kasha.intersection(ovsianaya_kasha)
if len(diff) == 0:
    print('Таких нет')
else:
    print(len(diff))
