n = int(input())
guests = set(input() for _ in range(n))

while True:
    guest = input()

    if guest == "END":
        break

    elif guest in guests:
        guests.remove(guest)

print(len(guests))
for _ in sorted(guests):
    print(_)
