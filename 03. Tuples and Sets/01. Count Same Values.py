numbers = [float(x) for x in input().split()]
occurs = {}


for number in numbers:
    count = numbers.count(number)
    if number not in occurs:
        occurs[number] = count

for key, value in occurs.items():
    print(f"{key} - {value} times")

