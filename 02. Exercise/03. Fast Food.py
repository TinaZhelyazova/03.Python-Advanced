from collections import deque

quantity_of_food = int(input())
integers = [int(x) for x in input().split()]

queue = deque()

for i in integers:
    queue.append(i)

print(max(queue))

for client_order in integers:
    if client_order <= quantity_of_food:
        quantity_of_food -= client_order
        queue.popleft()
    else:
        break

if len(queue) == 0:
    print("Orders complete")
else:
    print(f'Orders left: {" ". join([str(x) for x in queue])}')

