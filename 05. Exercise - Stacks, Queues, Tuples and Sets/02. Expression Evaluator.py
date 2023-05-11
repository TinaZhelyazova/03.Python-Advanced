from collections import deque

str_expression = [x for x in input().split()]
result = deque()

operations = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
    '/': lambda a, b: a // b,
}

for ch in str_expression:
    if ch in '+-*/':
        while len(result) > 1:
            num_a = result.popleft()
            num_b = result.popleft()
            number = operations[ch](num_a, num_b)
            result.appendleft(number)
    else:
        result.append(int(ch))

print(result.popleft())
