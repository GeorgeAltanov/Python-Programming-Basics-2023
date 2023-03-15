budget = float(input())
season = input()

place = None
destination = None
price = 0

if season == "summer":
    place = "Camp"
elif season == "winter":
    place = "Hotel"

if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        price = budget * 0.30
    else:
        price = budget * 0.70

elif budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        price = budget * 0.40
    else:
        price = budget * 0.80

elif budget > 1000:
    destination = "Europe"
    price = budget * 0.90
    place = "Hotel"

print(f"Somewhere in {destination} \n{place} - {price:.2f}")
