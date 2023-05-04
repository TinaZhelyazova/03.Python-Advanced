n = int(input())
data = set()
COMMAND_IN = "IN"
COMMAND_OUT = "OUT"

for i in range(n):
    command = input()
    direction, car_number = command.split(", ")

    if direction == COMMAND_IN:
        data.add(car_number)
    elif direction == COMMAND_OUT:
        data.remove(car_number)

if len(data) == 0:
    print(f"Parking Lot is Empty")
else:
    print("\n".join(data))
