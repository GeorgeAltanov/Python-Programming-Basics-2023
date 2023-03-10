from math import floor
from math import ceil

days = int(input())
food_kg = int(input())
dog_day_food = float(input())
cat_day_food = float(input())
turtle_day_food = float(input())

dog_food_needed = days * dog_day_food
cat_food_needed = days * cat_day_food
turtle_food_needed = days * turtle_day_food / 1000

total_food = dog_food_needed + cat_food_needed + turtle_food_needed

if total_food >= food_kg:
    print(f"{ceil(total_food - food_kg)} of food are needed.")
else:
    print(f"{floor(food_kg - total_food)} kilos of food left.")
