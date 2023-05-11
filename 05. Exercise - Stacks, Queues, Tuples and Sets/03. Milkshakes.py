from collections import deque

chocolates = [int(x) for x in input().split(", ")]
cup_of_milk = deque([int(x) for x in input().split(", ")])
milkshakes = 0

while milkshakes < 5 and chocolates and cup_of_milk:
    chocolate = chocolates.pop()
    milk = cup_of_milk.popleft()

    if chocolate <= 0 and milk <= 0:
        continue
    if chocolate <= 0:
        cup_of_milk.appendleft(milk)
        continue
    if milk <= 0:
        chocolates.append(chocolate)
        continue

    if chocolate == milk:
        milkshakes += 1
    else:
        cup_of_milk.append(milk)
        chocolates.append(chocolate - 5)


chocolate_to_str = [str(el) for el in chocolates]
milks = [str(el) for el in cup_of_milk]

if milkshakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")
if chocolates:
    print(f'Chocolate:', ", ".join(chocolate_to_str))
else:
    print("Chocolate: empty")
if cup_of_milk:
    print(f'Milk:', ", ".join(milks))
else:
    print("Milk: empty")

