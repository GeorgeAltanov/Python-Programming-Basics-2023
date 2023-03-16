chrysanthemums = int(input())
roses = int(input())
tulips = int(input())
season = input()
day = input()

total_price = 0

if season == "Spring" or season == "Summer":
    chrysanthemums_price = 2.00
    roses_price = 4.10
    tulips_price = 2.50
else:
    chrysanthemums_price = 3.75
    roses_price = 4.50
    tulips_price = 4.15

total_price = chrysanthemums * chrysanthemums_price + roses * roses_price + tulips * tulips_price

if day == "Y":
    total_price *= 1.15
if season == "Spring" and tulips > 7:
    total_price *= 0.95
if season == "Winter" and roses >= 10:
    total_price *= 0.90
if chrysanthemums + roses + tulips > 20:
    total_price *= 0.80

print(f"{total_price + 2:.2f}")
