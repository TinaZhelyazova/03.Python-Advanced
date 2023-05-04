n = int(input())
longest_intersection = set()

for i in range(n):
    first_half, second_half = [el.split(",") for el in input().split("-")]

    first_set = set(range(int(first_half[0]), int(first_half[1]) + 1))
    second_set = set(range(int(second_half[0]), int(second_half[1]) + 1))

    whole_set = first_set.intersection(second_set)

    if len(whole_set) > len(longest_intersection):
        longest_intersection = whole_set

numbers = [int(x) for x in longest_intersection]
print(f"Longest intersection is {numbers} with length {len(longest_intersection)}")

