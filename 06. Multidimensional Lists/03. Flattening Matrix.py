rows = int(input())
matrix = []

for row in range(rows):
    elements = [int(x) for x in input().split(',')]
    for el in elements:
        matrix.append(el)

print(matrix)
 