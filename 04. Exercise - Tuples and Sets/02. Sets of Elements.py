n, m = [int(x) for x in input().split()]
set_n = set()
set_m = set()

for first_elements in range(n):
    num_1 = int(input())
    set_n.add(num_1)

for second_elements in range(m):
    num_2 = int(input())
    set_m.add(num_2)

data = set_n.intersection(set_m)

for elements in data:
    print(elements)
