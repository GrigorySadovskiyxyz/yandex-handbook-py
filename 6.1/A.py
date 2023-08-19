import math

x = float(input())

log_part = math.log(pow(x, 3 / 16), 32)
cos_part = math.cos((math.pi * x) / (2 * math.e))
sin_part = math.sin(x / math.pi) ** 2

result = log_part + pow(x, cos_part) - sin_part

print(result)

