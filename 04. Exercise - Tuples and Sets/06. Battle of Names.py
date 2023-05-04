n = int(input())
counter_of_rows = 0
odd_set = set()
even_set = set()
result_numbers = []

for i in range(n):
    name = input()
    for char in name:
        number_of_char = ord(char)
        result_numbers.append(number_of_char)
    counter_of_rows += 1
    resulting_number = sum(result_numbers) // counter_of_rows
    if resulting_number % 2 == 0:
        even_set.add(resulting_number)
    else:
        odd_set.add(resulting_number)
    result_numbers = []

sum_odd_set = sum(odd_set)
sum_even_set = sum(even_set)

if sum_odd_set == sum_even_set:
    union_values = odd_set.union(even_set)
    print(*union_values, sep=", ")
elif sum_odd_set > sum_even_set:
    different_values = odd_set.difference(even_set)
    print(*different_values, sep=", ")
elif sum_even_set > sum_odd_set:
    symmetric_diff = even_set.symmetric_difference(odd_set)
    print(*symmetric_diff, sep=", ")
