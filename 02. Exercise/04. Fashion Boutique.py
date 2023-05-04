sequence_of_integers = [int(x) for x in input().split()]
capacity_of_one_rack = int(input())
counter = 1
capacity_of_one_rack_before_usage = capacity_of_one_rack
while len(sequence_of_integers) > 0:
    piece_of_clothing = sequence_of_integers[-1]

    if piece_of_clothing > capacity_of_one_rack_before_usage:
        counter+=1
        capacity_of_one_rack_before_usage = capacity_of_one_rack
    else:
        capacity_of_one_rack_before_usage -= piece_of_clothing
        sequence_of_integers.pop()

print(counter)
