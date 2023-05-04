text = input()
chars_count = {}

for char in text:
    if char not in chars_count:
        chars_count[char] = 1
        continue
    chars_count[char] += 1

for key, value in sorted(chars_count.items()):
    print(f"{key}: {value} time/s")
