a = int(input())
b = int(input())
copy_a = a
copy_b = b
NOD = b
while NOD != 0:
    NOD = b % a
    b = a
    a = NOD
print(int((copy_a * copy_b) / b))
