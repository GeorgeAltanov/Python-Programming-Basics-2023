month = input()
night_count = int(input())

total_price = 0

if month == "May" or month == "October":
    if night_count > 14:
        total_price = (night_count * 65) * 0.90
    else:
        total_price = night_count * 65
elif month == "June" or month == "September":
    if night_count > 14:
        total_price = (night_count * 68.70) * 0.90
    else:
        total_price = night_count * 68.70
if month == "July" or month == "August":
    if night_count > 14:
        total_price = (night_count * 77) * 0.90
    else:
        total_price = night_count * 77

print(f"Apartment: {total_price:.2f} lv.")

if month == "May" or month == "October":
    if 7 < night_count <= 14:
        total_price = (night_count * 50) * 0.95
    elif night_count > 14:
        total_price = (night_count * 50) * 0.70
    else:
        total_price = night_count * 50
elif month == "June" or month == "September":
    if night_count > 14:
        total_price = (night_count * 75.20) * 0.80
    else:
        total_price = night_count * 75.20
elif month == "July" or month == "August":
    total_price = night_count * 76

print(f"Studio: {total_price:.2f} lv.")
