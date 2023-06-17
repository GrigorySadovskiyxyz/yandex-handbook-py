while (n := input()) != '':
    if n.find('#') == 0:
        continue
    elif n.find('#') != -1:
        print(n[:n.find('#')])
    else:
        print(n)

