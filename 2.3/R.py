import math

number = int(input())
result = []

for i in range(2, number + 1):
    while (number % i == 0):
        result.append(str(i))
        number //= i

if (number != 1):
    print(number)

result = ' * '.join(result)
print(result)
