from itertools import combinations

nm = input().split()
total_variants = 0
vasya_variants = 0
N, M = nm[0], nm[1]

for combination in combinations(range(int(N)), int(M)):
    total_variants += 1
    if 0 in combination:
        vasya_variants += 1
print(int(vasya_variants), int(total_variants))
