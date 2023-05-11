from collections import deque

materials_in_one_box = [int(x) for x in input().split()]  # we should take the last box
magic_level = deque([int(x) for x in input().split()])  # we should take first magic level

total_magic_level = 0
doll = 150
wooden_train = 250
teddy_bear = 300
bicycle = 400

presents = {
    "Doll": 0,
    "Wooden train": 0,
    "Teddy bear": 0,
    "Bicycle": 0,
}

while materials_in_one_box and magic_level:
    materials = materials_in_one_box.pop()
    magic = magic_level.popleft()
    total_magic_level = materials * magic

    if materials == 0:
        magic_level.appendleft(magic)
    elif magic == 0:
        materials_in_one_box.append(materials)
    elif total_magic_level == doll:
        presents["Doll"] += 1
    elif total_magic_level == wooden_train:
        presents["Wooden train"] += 1
    elif total_magic_level == teddy_bear:
        presents["Teddy bear"] += 1
    elif total_magic_level == bicycle:
        presents["Bicycle"] += 1
    elif total_magic_level < 0:
        materials_in_one_box.append(materials + magic)
    elif total_magic_level > 0:
        materials_in_one_box.append(materials + 15)

    total_magic_level = 0

if (presents["Doll"] > 0 and presents["Wooden train"] > 0) or (presents["Teddy bear"] > 0 and presents["Bicycle"] > 0):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")
str_materials = [str(el) for el in materials_in_one_box]
str_magic = [str(el) for el in magic_level]
if materials_in_one_box:
    print(f'Materials left: {", ".join((reversed(str_materials)))}')
if magic_level:
    print(f'Magic left: {", ".join(str_magic)}')

for key, value in sorted(presents.items()):
    if value > 0:
        print(f"{key}: {value}")
