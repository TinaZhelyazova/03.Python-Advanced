n = int(input())
nicknames = set()

for i in range(n):
    name = input()
    nicknames.add(name)

print("\n".join(nicknames))
