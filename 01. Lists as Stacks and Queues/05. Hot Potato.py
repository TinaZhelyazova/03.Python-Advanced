from collections import deque

name = input().split()
step = int(input())

player_deque = deque(name)
counter = 0
while len(player_deque) > 1:
    counter += 1
    current_player = player_deque[0]

    if counter == step:
        print(f"Removed {player_deque.popleft()}")
        counter = 0
    else:
        player_deque.popleft()
        player_deque.append(current_player)
print(f'Last is {"".join(player_deque)}')
