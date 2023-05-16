rows, columns = [int(x) for x in input().split(', ')]
matrix = []
result = []
sum_for_result = 0

for row in range(rows):
    numbers = [int(x) for x in input().split()]
    matrix.append(numbers)

for i in range(len(matrix[0])):
    col_sum = 0
    for j in range(len(matrix)):
        col_sum += matrix[j][i]
    result.append(col_sum)

for el in result:
    print(el)

