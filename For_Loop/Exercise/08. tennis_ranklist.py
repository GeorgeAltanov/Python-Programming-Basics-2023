from math import floor

tourneys = int(input())
start_points = int(input())

W = 2000
F = 1200
SF = 720

points = 0
win = 0

for _ in range(tourneys):
    phase = input()
    if phase == "W":
        win += 1
        points += W
    elif phase == "F":
        points += F
    else:
        points += SF

print(f"Final points: {floor(points + start_points)}")
print(f"Average points: {floor(points / tourneys)}")
print(f"{win / tourneys * 100:.2f}%")
