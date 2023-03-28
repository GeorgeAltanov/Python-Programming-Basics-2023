player_1_eggs_count = int(input())
player_2_eggs_count = int(input())


while True:
    winner = input()
    if winner == "End":
        print(f"Player one has {player_1_eggs_count} eggs left.")
        print(f"Player two has {player_2_eggs_count} eggs left.")
        break
    if winner == "one":
        player_2_eggs_count -= 1
    elif winner == "two":
        player_1_eggs_count -= 1

    if player_1_eggs_count <= 0:
        print(f"Player one is out of eggs. Player two has {player_2_eggs_count} eggs left.")
        break
        
    elif player_2_eggs_count <= 0:
        print(f"Player two is out of eggs. Player one has {player_1_eggs_count} eggs left.")
        break
