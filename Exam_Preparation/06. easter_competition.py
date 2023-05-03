easter_bake = int(input())

winner_baker = None
max_points = 0

for _ in range(easter_bake):
    name_baker = input()
    points = 0
    condition = False

    while True:
        command = input()

        if command == "Stop":
            print(f"{name_baker} has {points} points.")
            break

        quantity = int(command)
        points += quantity

    if points > max_points:
        max_points = points
        winner_baker = name_baker
        print(f"{winner_baker} is the new number 1!")

print(f"{winner_baker} won competition with {max_points} points!")
