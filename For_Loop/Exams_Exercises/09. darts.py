player = input()

start_points = 301
shots = 0
unsuccessful_shots = 0

while True:

    zone = input()

    if zone == "Retire":
        print(f"{player} retired after {unsuccessful_shots} unsuccessful shots.")
        break

    points = int(input())

    if zone == "Triple":
        points *= 3
        if points <= start_points:
            start_points -= points
            shots += 1
        else:
            unsuccessful_shots += 1
    elif zone == "Double":
        points *= 2
        if points <= start_points:
            start_points -= points
            shots += 1
        else:
            unsuccessful_shots += 1
    elif zone == "Single":
        points = points
        if points <= start_points:
            start_points -= points
            shots += 1
        else:
            unsuccessful_shots += 1

    if start_points == 0:
        print(f"{player} won the leg with {shots} shots.")
        break
