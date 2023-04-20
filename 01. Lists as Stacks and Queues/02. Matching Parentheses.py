expression = input()
stack = []

for i in range(len(expression)):

    if expression[i] == "(":
        stack.append(i)
    elif expression[i] == ")":
        expr_for_print = expression[stack.pop():i+1]
        print(expr_for_print)

