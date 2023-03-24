students_count = int(input())

fail_students = 0
average_students = 0
good_students = 0
top_students = 0
average_grades = 0

for _ in range(students_count):
    grades = float(input())
    average_grades += grades / students_count
    if grades <= 2.99:
        fail_students += 1
    elif grades <= 3.99:
        average_students += 1
    elif grades <= 4.99:
        good_students += 1
    else:
        top_students += 1

print(f"Top students: {top_students / students_count * 100:.2f}%")
print(f"Between 4.00 and 4.99: {good_students / students_count * 100:.2f}%")
print(f"Between 3.00 and 3.99: {average_students / students_count * 100:.2f}%")
print(f"Fail: {fail_students / students_count * 100:.2f}%")
print(f"Average: {average_grades:.2f}")
