type_of_flowers = input()
quantity_flowers = int(input())
budget = int(input())

ROSES = 5.00
DAHLIAS = 3.80
TULIPS = 2.80
NARCISSUS = 3.00
GLADIOLUS = 2.50

total_price = 0

if type_of_flowers == "Roses":
    total_price = quantity_flowers * ROSES

    if quantity_flowers > 80:
        total_price *= 0.90

elif type_of_flowers == "Dahlias":
    total_price = quantity_flowers * DAHLIAS

    if quantity_flowers > 90:
        total_price *= 0.85

elif type_of_flowers == "Tulips":
    total_price = quantity_flowers * TULIPS

    if quantity_flowers > 80:
        total_price *= 0.85

elif type_of_flowers == "Narcissus":
    total_price = quantity_flowers * NARCISSUS

    if quantity_flowers < 120:
        total_price *= 1.15

elif type_of_flowers == "Gladiolus":
    total_price = quantity_flowers * GLADIOLUS

    if quantity_flowers < 80:
        total_price *= 1.20

if budget >= total_price:
    print(f"Hey, you have a great garden with {quantity_flowers} {type_of_flowers} and {budget - total_price:.2f} leva left.")

else:
    print(f"Not enough money, you need {total_price - budget:.2f} leva more.")
