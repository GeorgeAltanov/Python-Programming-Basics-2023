from math import ceil

easter_bred = int(input())

SUGAR_PACKET = 950
FLOUR_PACKET = 750

max_sugar_quantity = 0
max_flour_quantity = 0
easter_bred_count = 0
total_sugar_needed = 0
total_flour_needed = 0

total_sugar_packet = 0
total_flour_packet = 0

while easter_bred_count != easter_bred:

    sugar_needed = int(input())
    flour_needed = int(input())

    total_sugar_needed += sugar_needed
    total_flour_needed += flour_needed

    if sugar_needed >= max_sugar_quantity:
        max_sugar_quantity = sugar_needed

    if flour_needed >= max_flour_quantity:
        max_flour_quantity = flour_needed

    easter_bred_count += 1

total_sugar_packet = ceil(total_sugar_needed / SUGAR_PACKET)
total_flour_packet = ceil(total_flour_needed / FLOUR_PACKET)
print(f"Sugar: {total_sugar_packet}")
print(f"Flour: {total_flour_packet}")
print(f"Max used flour is {max_flour_quantity} grams, max used sugar is {max_sugar_quantity} grams.")
