name_team = input()
derby_count = int(input())

total_derby = 0
win = 0
equality = 0
loss = 0
total_points = 0

if derby_count == 0:
    print(f"{name_team} hasn't played any games during this season.")
while total_derby < derby_count:
    result = input()

    if result == "W":
        win += 1
    elif result == "D":
        equality += 1
    elif result == "L":
        loss += 1
    total_derby += 1
total_points = 3 * win + equality

if derby_count >= 1:
    print(f"{name_team} has won {total_points} points during this season.")
    print(f"Total stats:\n## W: {win}\n## D: {equality}\n## L: {loss}\nWin rate: {win / total_derby * 100:.2f}%")
