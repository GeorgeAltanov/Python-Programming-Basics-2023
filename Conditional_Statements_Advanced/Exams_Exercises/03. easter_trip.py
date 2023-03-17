destination = input()
date = input()
night = int(input())

price_per_night = 0

if destination == "France":
    if date == "21-23":
        price_per_night += 30
    elif date == "24-27":
        price_per_night += 35
    elif date == "28-31":
        price_per_night += 40

elif destination == "Italy":
    if date == "21-23":
        price_per_night += 28
    elif date == "24-27":
        price_per_night += 32
    elif date == "28-31":
        price_per_night += 39

elif destination == "Germany":
    if date == "21-23":
        price_per_night += 32
    elif date == "24-27":
        price_per_night += 37
    elif date == "28-31":
        price_per_night += 43

total_price = price_per_night * night
print(f"Easter trip to {destination} : {total_price:.2f} leva.")
