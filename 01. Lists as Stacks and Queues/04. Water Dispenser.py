from collections import deque
quantity_of_water = int(input())
queue = deque([])
while True:
    command = input()

    if command == "Start":
        break
    queue.appendleft(command)

while True:
    command = input().split()
    if command[0] == "End":
        break
    elif command[0] == "refill":
        liters = int(command[1])
        quantity_of_water += liters
    else:
        # there will be only the liters
        if int(command[0]) <= quantity_of_water:
            print(f"{queue.pop()} got water")
            quantity_of_water -= int(command[0])
            continue
        else:
            print(f"{queue.pop()} must wait")
            continue

print(f"{quantity_of_water} liters left")
