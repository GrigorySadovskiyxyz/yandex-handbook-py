def only_positive_even_sum(num1, num2):
    if type(num1) is not int or type(num2) is not int:
        raise TypeError
    if not (num1 > 0 and not num1 % 2) or not (num2 > 0 and not num2 % 2):
        raise ValueError
    return num1 + num2
