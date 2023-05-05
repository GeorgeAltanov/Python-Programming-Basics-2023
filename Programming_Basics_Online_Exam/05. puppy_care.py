food = int(input()) * 1000

total_puppy_food = 0

while True:
    puppy_food = input()

    if puppy_food == "Adopted":
        break

    puppy_food = int(puppy_food)

    total_puppy_food += puppy_food

if total_puppy_food <= food:
    print(f"Food is enough! Leftovers: {food - total_puppy_food} grams.")

else:
    print(f"Food is not enough. You need {total_puppy_food - food} grams more.")
