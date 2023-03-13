budget = float(input())
nights = int(input())
price_per_night = float(input())
extra_expenses = int(input())

total_price_per_night = 0

if nights > 7:
    price_per_night *= 0.95

extra_expenses *= budget / 100
total_price_per_night = (price_per_night * nights) + extra_expenses


if total_price_per_night <= budget:
    print(f"Ivanovi will be left with {budget - total_price_per_night:.2f} leva after vacation.")

else:
    print(f"{total_price_per_night - budget:.2f} leva needed.")
