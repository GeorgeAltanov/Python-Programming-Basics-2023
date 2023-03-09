excursion_price = float(input())
puzzles_quantity = int(input())
dolls_quantity = int(input())
bears_quantity = int(input())
minions_quantity = int(input())
trucks_quantity = int(input())

PUZZLES_PRICE = 2.60
DOLLS_PRICE = 3.00
BEARS_PRICE = 4.10
MINIONS_PRICE = 8.20
TRUCKS_PRICE = 2.00
STORE_RENT = 0.10

quantity_toys = puzzles_quantity + dolls_quantity + bears_quantity + minions_quantity + trucks_quantity
total_price = puzzles_quantity * PUZZLES_PRICE + dolls_quantity * DOLLS_PRICE + bears_quantity * BEARS_PRICE\
            + minions_quantity * MINIONS_PRICE + trucks_quantity * TRUCKS_PRICE

if quantity_toys >= 50:
    total_price *= 0.75

total_price *= 0.90

if total_price >= excursion_price:
    print(f"Yes! {total_price - excursion_price:.2f} lv left.")

else:
    print(f"Not enough money! {excursion_price - total_price:.2f} lv needed.")
