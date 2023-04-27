customer = int(input())

BASKET = 1.50
WREATH = 3.80
CHOCOLATE_BUNNY = 7.00

average_bill = 0
counter = 0

while counter != customer:

    bill = 0
    purchase_count = 0
    while True:
        purchase = input()

        if purchase == "Finish":
            if purchase_count % 2 == 0:
                bill *= 0.80
            average_bill += bill
            print(f"You purchased {purchase_count} items for {bill:.2f} leva.")
            break

        if purchase == "basket":
            bill += BASKET
        elif purchase == "wreath":
            bill += WREATH
        elif purchase == "chocolate bunny":
            bill += CHOCOLATE_BUNNY

        purchase_count += 1
    counter += 1

print(f"Average bill per client is: {average_bill / customer:.2f} leva.")
