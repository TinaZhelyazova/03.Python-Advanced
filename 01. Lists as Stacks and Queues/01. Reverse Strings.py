string = input()
stack = []
for i in string:
    stack.append(i)

stack.reverse()
print("".join(stack))
