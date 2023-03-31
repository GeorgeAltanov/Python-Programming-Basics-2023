fail_grades_count = int(input())

total_grades = 0
task_count = 0
poor_grades_count = 0
last_task = None

while True:
    name_task = input()
    if name_task == "Enough":
        print(f"Average score: {total_grades / task_count:.2f}")
        print(f"Number of problems: {task_count}")
        print(f"Last problem: {last_task}")
        break
    task_count += 1
    last_task = name_task
    score = int(input())
    total_grades += score

    if score <= 4:
        poor_grades_count += 1
        if poor_grades_count >= fail_grades_count:
            print(f"You need a break, {poor_grades_count} poor grades.")
            break
