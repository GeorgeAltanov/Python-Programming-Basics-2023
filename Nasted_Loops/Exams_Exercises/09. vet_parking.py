days = int(input())
hours = int(input())

counter = 0
total_price = 0
price = 0

for day in range(1, days + 1):
    price_1 = 0
    price_2 = 0

    for hour in range(1, hours + 1):

        if day % 2 == day % 2 == 1 and hour % 2 == 0:
            price = 1.25
            price_2 += price
            total_price += price

        elif day % 2 == 1:
            price = 1.00
            price_2 += price
            total_price += price

        if day % 2 == 0 and hour % 2 == 1:
            price = 2.50
            price_1 += price
            total_price += price

        elif day % 2 == 0:
            price = 1.00
            price_1 += price
            total_price += price

        counter += 1

    if day % 2 == 1:
        print(f"Day: {day} - {price_2:.2f} leva")
    elif day % 2 == 0:
        print(f"Day: {day} - {price_1:.2f} leva")

    if counter == day:
        break

print(f"Total: {total_price:.2f} leva")
