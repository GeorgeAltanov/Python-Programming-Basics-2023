distance_km = int(input())
time_of_travel = input()

price = 0

if distance_km < 20:
    if time_of_travel == "day":
        price = 0.70 + distance_km * 0.79
    else:
        price = 0.70 + distance_km * 0.90
elif 20 <= distance_km < 100:
    price = distance_km * 0.09
else:
    price = distance_km * 0.06

print(f"{price:.2f}")
