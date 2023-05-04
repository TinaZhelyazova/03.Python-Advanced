n = int(input())
data = {}

for student in range(n):
    student_data = input()
    name, grade = student_data.split()

    if name not in data:
        data[name] = []
    data[name].append(float(grade))

for key, value in data.items():
    avr_grade = sum(value) / len(value)
    formatted_grade = map(lambda x: f'{x:.2f}', value)
    grade_to_str = " ".join([str(x) for x in formatted_grade])
    print(f"{key} -> {grade_to_str} (avg: {avr_grade:.2f})")
