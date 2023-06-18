def recursive_digit_sum(n):
    if n == 0:
        return 0
    else: 
        return recursive_digit_sum(n // 10) + n % 10
