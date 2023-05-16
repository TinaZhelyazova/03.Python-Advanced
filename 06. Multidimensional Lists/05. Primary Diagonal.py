n = int(input())
matrix = []
result = 0

for i in range(n):
    numbers = [int(x) for x in input().split()]
    matrix.append(numbers)

for row in range(len(matrix)):
    for el in range(len(matrix[0])):
        if row == el:
            curr_el = matrix[row][el]
            result += curr_el

print(result)
