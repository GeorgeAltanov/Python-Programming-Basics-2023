win = 0
loss = 0
count_game = 0

while True:
    name_tournament = input()

    if name_tournament == "End of tournaments":
        print(f"{win / count_game * 100:.2f}% matches win")
        print(f"{loss / count_game * 100:.2f}% matches lost")
        break

    game = int(input())
    count_game += game
    number_of_game = 0

    for i in range(game):
        points_Desi = int(input())
        another_team_points = int(input())

        if points_Desi > another_team_points:
            number_of_game += 1
            print(
                f"Game {number_of_game} of tournament {name_tournament}: win with {points_Desi - another_team_points}"
                f" points.")
            win += 1
        elif points_Desi < another_team_points:
            number_of_game += 1
            print(
                f"Game {number_of_game} of tournament {name_tournament}: lost with {another_team_points - points_Desi}"
                f" points.")
            loss += 1
