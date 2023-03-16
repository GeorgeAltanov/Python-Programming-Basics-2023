budget = float(input())
season = input()

car = None
price = 0
class_car = None

if budget <= 100:
    class_car = "Economy class"
    if season == "Summer":
        car = "Cabrio"
        budget *= 0.35
    else:
        car = "Jeep"
        budget *= 0.65

elif budget <= 500:
    class_car = "Compact class"
    if season == "Summer":
        car = "Cabrio"
        budget *= 0.45
    else:
        car = "Jeep"
        budget *= 0.80
else:
    class_car = "Luxury class"
    car = "Jeep"
    budget *= 0.90

print(f"{class_car}\n{car} - {budget:.2f}")
