rows, columns = [int(x) for x in input().split(", ")]
curr_sum = 0
matrix = []

for row in range(rows):
    numbers = [int(x) for x in input().split(', ')]
    matrix.append(numbers)
    curr_sum += sum(numbers)

print(curr_sum)
print(matrix)
