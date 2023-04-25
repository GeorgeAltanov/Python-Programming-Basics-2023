name = input()

name_winner = None
max_points = 0

while name != "Stop":
    points = 0

    for char in name:
        number = int(input())
        if ord(char) == number:
            points += 10
        else:
            points += 2

        if points >= max_points:
            max_points = points
            name_winner = name

    name = input()
print(f"The winner is {name_winner} with {max_points} points!")
