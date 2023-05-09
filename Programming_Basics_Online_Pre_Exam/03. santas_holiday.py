days = int(input())
place = input()
grade = input()

ROOM_FOR_ONE_PERSON = 18.00
APARTMENT = 25.00
PRESIDENT_APARTMENT = 35.00

night = days -1
price = 0

if place == "room for one person":
    price = night * ROOM_FOR_ONE_PERSON
elif place == "apartment":
    price = night * APARTMENT
    if night < 10:
        price *= 0.70
    elif 10 <= night < 15:
        price *= 0.65
    elif night >= 15:
        price *= 0.50

elif place == "president apartment":
    price = night * PRESIDENT_APARTMENT
    if night < 10:
        price *= 0.90
    elif 10 <= night < 15:
        price *= 0.85
    elif night >= 15:
        price *= 0.80

if grade == "positive":
    price *= 1.25
elif grade == "negative":
    price *= 0.90

print(f"{price:.2f}")
