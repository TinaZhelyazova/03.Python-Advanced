stack = []
n = int(input())

for i in range(n):
    query = [int(x) for x in input().split()]
    command = query[0]

    if command == 1:
        number = query[1]
        stack.append(number)
    elif command == 2 and len(stack) > 0:
        stack.pop()
    elif command == 3 and len(stack) > 0:
        print(max(stack))
    elif command == 4 and len(stack) > 0:
        print(min(stack))

stack.reverse()

print(*stack, sep=", ")
