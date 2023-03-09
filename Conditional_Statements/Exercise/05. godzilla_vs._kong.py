budget_film = float(input())
number_of_statistics = int(input())
cost_of_clothing_for_statistic = float(input())

decor_for_the_film = budget_film * 0.10
total_expenses = decor_for_the_film + number_of_statistics * cost_of_clothing_for_statistic

if number_of_statistics >= 150:
    cost_of_clothing_for_statistic *= 0.90

total_expenses = decor_for_the_film + number_of_statistics * cost_of_clothing_for_statistic

if total_expenses <= budget_film:
    print("Action!")
    print(f"Wingard starts filming with {budget_film - total_expenses:.2f} leva left.")

else:
    print("Not enough money!")
    print(f"Wingard needs {total_expenses - budget_film:.2f} leva more.")
