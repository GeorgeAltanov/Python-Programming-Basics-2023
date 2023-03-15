days_to_stay = int(input()) - 1
type_of_room = input()
rating = input()

ROOM_FOR_ONE_PERSON = 18.00
APARTMENT = 25.00
PRESIDENT_APARTMENT = 35.00

total_price = 0

if type_of_room == "room for one person":
    if days_to_stay < 10:
        total_price = days_to_stay * ROOM_FOR_ONE_PERSON
    elif 10 <= days_to_stay <= 15:
        total_price = days_to_stay * ROOM_FOR_ONE_PERSON
    else:
        total_price = days_to_stay * ROOM_FOR_ONE_PERSON

if type_of_room == "apartment":
    if days_to_stay < 10:
        total_price = days_to_stay * APARTMENT * 0.70
    elif 10 <= days_to_stay <= 15:
        total_price = days_to_stay * APARTMENT * 0.65
    else:
        total_price = days_to_stay * APARTMENT * 0.50

if type_of_room == "president apartment":
    if days_to_stay < 10:
        total_price = days_to_stay * PRESIDENT_APARTMENT * 0.90
    elif 10 <= days_to_stay <= 15:
        total_price = days_to_stay * PRESIDENT_APARTMENT * 0.85
    else:
        total_price = days_to_stay * PRESIDENT_APARTMENT * 0.80

if rating == "positive":
    total_price *= 1.25
else:
    total_price *= 0.90

print(f"{total_price:.2f}")
