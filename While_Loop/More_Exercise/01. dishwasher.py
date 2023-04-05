bottles = int(input())

DETERGENT_BOTTLES = 750
DETERGENT_DISHES = 5
DETERGENT_POTS = 15
counter = 0
detergent = bottles * DETERGENT_BOTTLES
dishes_count = 0
pots_count = 0

while detergent >= 0:
    quantity = input()
    counter += 1

    if quantity == "End":
        break

    quantity = int(quantity)

    if counter % 3 != 0:
        used_detergent_dishes = quantity * DETERGENT_DISHES
        detergent -= used_detergent_dishes
        dishes_count += quantity

    else:
        used_detergent_pots = quantity * DETERGENT_POTS
        detergent -= used_detergent_pots
        pots_count += quantity

if detergent >= 0:
    print("Detergent was enough!")
    print(f"{dishes_count} dishes and {pots_count} pots were washed.")
    print(f"Leftover detergent {detergent} ml.")

else:
    print(f"Not enough detergent, {abs(detergent)} ml. more necessary!")
