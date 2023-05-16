
n = int(input())
matrix = []
is_valid = True

for row in range(n):
    row_data = list(input())
    matrix.append(row_data)

character = input()
for row in range(len(matrix)):
    for el in range(len(matrix[row])):
        curr_el = matrix[row][el]
        if character == curr_el:
            print(f"({row}, {el})")
            is_valid = False


if is_valid:
    print(f"{character} does not occur in the matrix")
