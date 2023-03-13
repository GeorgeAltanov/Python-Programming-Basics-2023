budget = float(input())
actor = int(input())
price_clothing = float(input())

money = 0
decor_price = budget * 0.10
total_price_clothing = actor * price_clothing
if actor > 150:
    total_price_clothing *= 0.90

total_money_needed = decor_price + total_price_clothing

if total_money_needed > budget:
    print(f"Not enough money!\nWingard needs {total_money_needed - budget:.2f} leva more.")
else:
    print(f"Action!\nWingard starts filming with {budget - total_money_needed:.2f} leva left.")
