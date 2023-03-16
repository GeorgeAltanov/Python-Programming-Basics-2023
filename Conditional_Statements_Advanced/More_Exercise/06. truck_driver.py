season = input()
month_km = float(input())

salary = 0
fee = 0.90
month = 4

if month_km <= 5000:
    if season == "Spring" or season == "Autumn":
        salary = month * month_km * 0.75
    elif season == "Summer":
        salary = month * month_km * 0.90
    else:
        salary = month * month_km * 1.05
elif month_km <= 10000:
    if season == "Spring" or season == "Autumn":
        salary = month * month_km * 0.95
    elif season == "Summer":
        salary = month * month_km * 1.10
    else:
        salary = month * month_km * 1.25
elif month_km <= 20000:
    salary = month * month_km * 1.45

print(f"{salary * fee:.2f}")
