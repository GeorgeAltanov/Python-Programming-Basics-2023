budget = float(input())

product_price = 0
counter_product = 0
total_price = 0

while True:
    product = input()

    if product == "Stop":
        print(f"You bought {counter_product} products for {total_price:.2f} leva.")
        break

    counter_product += 1
    product_price = float(input())
    if counter_product % 3 == 0:
        product_price /= 2

    if product_price > budget:
        print(f"You don't have enough money!")
        print(f"You need {product_price - budget:.2f} leva!")
        break

    budget -= product_price

    total_price += product_price
