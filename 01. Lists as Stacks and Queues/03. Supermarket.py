from collections import deque
queue = deque([])

while True:
    name = input()
    if name == "End":
        break
    elif name == "Paid":
        queue.reverse()
        print("\n".join(queue))
        queue.clear()
        continue

    queue.appendleft(name)


print(f"{len(queue)} people remaining.")
