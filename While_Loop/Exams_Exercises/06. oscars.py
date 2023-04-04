actor = input()
points_from_academy = float(input())
judges_count = int(input())

WIN_POINTS = 1250.50
points = 0
counter_judges = 0

for _ in range(judges_count):

    name_of_judge = input()
    points_from_judge = float(input())

    length_of_judge = len(name_of_judge)
    points = length_of_judge * points_from_judge / 2
    points_from_academy += points

    counter_judges += 1

    if points_from_academy >= WIN_POINTS:
        break

if points_from_academy < WIN_POINTS:
    print(f"Sorry, {actor} you need {WIN_POINTS - points_from_academy:.1f} more!")

else:
    print(f"Congratulations, {actor} got a nominee for leading role with {points_from_academy:.1f}!")
