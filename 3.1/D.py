while (n := input()) != '':
    if n.endswith('@@@'):
        continue
    elif n.startswith('##'):
        print(n[2:])
    else:
        print(n)

