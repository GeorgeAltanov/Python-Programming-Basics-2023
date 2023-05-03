budget = float(input())
needed_oil = float(input())
day_of_week = input()

OIL_PRICE = 2.10
TOUR_GUIDE = 100

oil_price = needed_oil * OIL_PRICE
total_price = oil_price + TOUR_GUIDE

if day_of_week == "Sunday":
    total_price *= 0.80
elif day_of_week == "Saturday":
    total_price *= 0.90

if budget >= total_price:
    print(f"Safari time! Money left: {budget - total_price:.2f} lv.")

else:
    print(f"Not enough money! Money needed: {total_price - budget:.2f} lv.")
