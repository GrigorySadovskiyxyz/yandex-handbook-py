n = list(input().replace(' ', ''))
operations = '+-*'
stack = []
for i, x in enumerate(n):
    if x.isalnum():
        stack.append(x)
        print(stack)
    elif operations.find(x) != -1:
        stack_add = eval(f'{stack[i - 2]} {x} {stack[i - 1]}')
        print(stack_add)
        stack.pop()
        stack.pop()
        print(stack)
        stack.append(stack_add)
print(stack)

