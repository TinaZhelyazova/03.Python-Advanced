from collections import deque


def robots_input():
    result = {}
    data = input().split(";")
    for robot in data:
        robot_details = robot.split("-")
        robot_name = robot_details[0]
        seconds_of_robot_work = int(robot_details[1])
        result[robot_name] = seconds_of_robot_work
    return result


def to_seconds(hours, minutes, seconds):
    return hours * 60 * 60 + minutes * 60 + seconds


def read_products():
    result = deque()
    while True:
        line = input()
        if line == "End":
            break
        result.append(line)
    return result


def to_str_time(time_in_seconds):
    hours = time_in_seconds // 3600
    minutes = (time_in_seconds % 3600) // 60
    seconds = (time_in_seconds % 3600) % 60
    return f'{hours:02d}:{minutes:02d}:{seconds:02d}'


robots = robots_input()
available_robots = [key for key in robots.keys()]
processing_robots = {}

starting_time_parts = [int(x) for x in input().split(":")]
time_in_seconds = to_seconds(starting_time_parts[0], starting_time_parts[1], starting_time_parts[2])

products = read_products()

while products:
    time_in_seconds = (time_in_seconds+1) % (24*60*60)
    current_product = products.popleft()

    for robot_name in [k for k in processing_robots.keys()]:
        processing_robots[robot_name] -= 1
        if processing_robots[robot_name] <= 0:
            processing_robots.pop(robot_name)

    for robot_name in available_robots:
        if robot_name not in processing_robots:
            print(f'{robot_name} - {current_product} [{to_str_time(time_in_seconds)}]')
            processing_robots[robot_name] = robots[robot_name]
            break
    else:
        products.append(current_product)
