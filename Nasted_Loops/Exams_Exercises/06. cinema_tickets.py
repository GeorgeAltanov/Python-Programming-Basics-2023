students_tickets_total = 0
standard_tickets_total = 0
kids_tickets_total = 0

while True:
    movie_name = input()
    if movie_name == "Finish":
        break
    seats = int(input())

    student_ticket = 0
    standard_ticket = 0
    kids_ticket = 0
    total_tickets_movie = 0

    while total_tickets_movie != seats:
        ticket = input()
        if ticket == "End":
            break
        if ticket == "student":
            student_ticket += 1
            students_tickets_total += 1
        elif ticket == "standard":
            standard_ticket += 1
            standard_tickets_total += 1
        elif ticket == "kid":
            kids_ticket += 1
            kids_tickets_total += 1
        total_tickets_movie += 1

    print(f"{movie_name} - {total_tickets_movie / seats * 100:.2f}% full.")

total_tickets = students_tickets_total + standard_tickets_total + kids_tickets_total
print(f"Total tickets: {total_tickets}")
print(f"{students_tickets_total / total_tickets * 100:.2f}% student tickets.")
print(f"{standard_tickets_total / total_tickets * 100:.2f}% standard tickets.")
print(f"{kids_tickets_total / total_tickets * 100:.2f}% kids tickets.")
