students_name = input()

class_of_students = 0
fail_grades = 0
average_grades = 0

while True:
    grades = float(input())

    if grades < 4:
        fail_grades += 1
        if fail_grades == 2:
            print(f"{students_name} has been excluded at {class_of_students + 1} grade")
            break

    else:
        class_of_students += 1
        average_grades += grades

        if class_of_students == 12:
            print(f"{students_name} graduated. Average grade: {average_grades / class_of_students :.2f}")
            break
