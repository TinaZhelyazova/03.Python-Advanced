set_one = set(int(x) for x in input().split())
set_two = set(int(x) for x in input().split())
n = int(input())

for _ in range(n):
    operation, *data = input().split()
    command = operation + " " + data.pop(0)

    if command == "Add First":
        [set_one.add(int(el)) for el in data]
    elif command == "Add Second":
        [set_two.add(int(el)) for el in data]
    elif command == "Remove First":
        [set_one.discard(int(el)) for el in data]
    elif command == "Remove Second":
        [set_two.discard(int(el)) for el in data]
    elif command == "Check Subset":
        if set_one.issubset(set_two) or set_two.issubset(set_one):
            print(True)
        else:
            print(False)

print(*sorted(set_one), sep=", ")
print(*sorted(set_two), sep=", ")
