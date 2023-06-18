def recursive_sum(one, *args):
    if len(args) == 0:
        return one
    else:
        return recursive_sum(*args) + int(one)
