from math import ceil

people = int(input())
entrance_fee = float(input())
sun_lounger_price = float(input())
umbrella_price = float(input())

total_sun_lounger_price = (ceil(people * 0.75)) * sun_lounger_price
total_umbrella_price = (ceil(people / 2)) * umbrella_price
total_entrance_fee = people * entrance_fee

total_price = total_entrance_fee + total_sun_lounger_price + total_umbrella_price

print(f"{total_price:.2f} lv.")
