from math import ceil

guests = int(input())
budget = int(input())

BREAD_PRICE = 4.00
EGG_PRICE = 0.45

bread_count = ceil(guests / 3)
eggs_count = guests * 2
bread_total_price = bread_count * BREAD_PRICE
eggs_total_price = eggs_count * EGG_PRICE
total_price = bread_total_price + eggs_total_price

if total_price <= budget:
    print(f"Lyubo bought {bread_count} Easter bread and {eggs_count} eggs.")
    print(f"He has {budget - total_price:.2f} lv. left.")
else:
    print("Lyubo doesn't have enough money.")
    print(f"He needs {total_price - budget:.2f} lv. more.")
