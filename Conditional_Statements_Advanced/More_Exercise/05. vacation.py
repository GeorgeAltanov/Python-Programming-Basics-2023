budget = float(input())
season = input()

location = None
place_for_life = None

if budget <= 1000:
    place_for_life = "Camp"
    if season == "Summer":
        location = "Alaska"
        budget *= 0.65
    else:
        location = "Morocco"
        budget *= 0.45
elif budget <= 3000:
    place_for_life = "Hut"
    if season == "Summer":
        location = "Alaska"
        budget *= 0.80
    else:
        location = "Morocco"
        budget *= 0.60
else:
    place_for_life = "Hotel"
    if season == "Summer":
        location = "Alaska"
    else:
        location = "Morocco"
    budget *= 0.90

print(f"{location} - {place_for_life} - {budget:.2f}")
