from collections import deque

working_bees = deque([int(x) for x in input().split()])
collected_nectar = [int(x) for x in input().split()]
symbols = deque([x for x in input().split()])

honey = 0

honey_calc = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a / b,

}

while working_bees and collected_nectar:
    bee = working_bees.popleft()
    nectar = collected_nectar.pop()

    if nectar >= bee:
        working_bees.append(bee)
        symbol = symbols.popleft()
        honey += abs(honey_calc[symbol](bee, nectar))
        working_bees.pop()

    if nectar < bee:
        working_bees.appendleft(bee)
        continue

print(f"Total honey made: {honey}")
if working_bees:
    print(f'Bees left: {", ".join(str(el) for el in working_bees)}')
if collected_nectar:
    print(f'Nectar left: {", ".join(str(el) for el in collected_nectar)}')
