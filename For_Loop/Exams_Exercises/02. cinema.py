capacity = int(input())

TICKETS = 5
total_people = 0
price = 0

condition = False

while True:
    people_coming = input()

    if people_coming == "Movie time!":
        condition = True
        break

    people_coming = int(people_coming)
    total_people += people_coming

    if total_people > capacity:
        print("The cinema is full.")
        break

    if people_coming % 3 == 0:
        price -= 5

    price += TICKETS * people_coming

if condition:
    print(f"There are {capacity - total_people} seats left in the cinema.")

print(f"Cinema income - {price} lv.")
