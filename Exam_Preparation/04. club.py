profit = float(input())

total_price = 0
PARTY_CONDITION = False
while total_price < profit:

    name_of_cocktails = input()
    price_of_cocktails = len(name_of_cocktails)

    if name_of_cocktails == "Party!":
        PARTY_CONDITION = True
        break

    cocktails_quantity = int(input())

    price_sum = price_of_cocktails * cocktails_quantity

    if price_sum % 2 != 0:
        price_sum *= 0.75

    total_price += price_sum

if PARTY_CONDITION:
    print(f"We need {profit - total_price:.2f} leva more.")

elif total_price >= profit:
    print("Target acquired.")

print(f"Club income - {total_price:.2f} leva.")
