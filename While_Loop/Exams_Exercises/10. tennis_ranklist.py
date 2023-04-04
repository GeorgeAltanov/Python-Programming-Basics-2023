from math import floor

count_tourneys = int(input())
start_points = int(input())

count_of_win_tourneys = 0
total_points = 0

for tourneys in range(count_tourneys):
    stage_of_the_tournament = input()

    if stage_of_the_tournament == "W":
        total_points += 2000
        count_of_win_tourneys += 1
    elif stage_of_the_tournament == "F":
        total_points += 1200
    elif stage_of_the_tournament == "SF":
        total_points += 720

print(f"Final points: {start_points + total_points}")
print(f"Average points: {floor(total_points / count_tourneys)}")
print(f"{count_of_win_tourneys / count_tourneys * 100:.2f}%")
