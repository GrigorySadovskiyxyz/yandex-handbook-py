from math import prod

nums = [float(x) for x in input().split()]

n = len(nums)
print(prod(nums) ** (1 / n))
