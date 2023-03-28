profit = float(input())

total_sum = 0
while True:
    cocktail = input()

    if cocktail == "Party!":
        print(f"We need {profit - total_sum:.2f} leva more.")
        break
    count = int(input())
    price_cocktail = len(cocktail)
    price_order = price_cocktail * count

    if price_order % 2 == 1:
        price_order *= 0.75

    total_sum += price_order

    if total_sum >= profit:
        print("Target acquired.")
        break
        
print(f"Club income - {total_sum:.2f} leva.")
