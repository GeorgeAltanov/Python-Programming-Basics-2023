from math import floor
from math import ceil

vineyard_sq_m = int(input())
grapes_sq_m = float(input())
liters_of_wine_needed = int(input())
workers = int(input())

total_grapes = vineyard_sq_m * grapes_sq_m
wine = total_grapes / 2.5 * 0.40

if wine >= liters_of_wine_needed:
    rest_wine = wine - liters_of_wine_needed
    print(f"Good harvest this year! Total wine: {floor(wine)} liters.")
    print(f"{ceil(rest_wine)} liters left -> {ceil(rest_wine / workers)} liters per person.")

else:
    print(f"It will be a tough winter! More {floor(liters_of_wine_needed - wine)} liters wine needed.")
