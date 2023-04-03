quantity_eggs = int(input())

max_eggs = 0
name_max_eggs = None
red_eggs = 0
orange_eggs = 0
blue_eggs = 0
green_eggs = 0

counter_eggs = 0
while counter_eggs != quantity_eggs:

    colour_eggs = input()

    if colour_eggs == "red":
        red_eggs += 1
        if red_eggs > max_eggs:
            max_eggs = red_eggs
            name_max_eggs = "red"

    elif colour_eggs == "orange":
        orange_eggs += 1
        if orange_eggs > max_eggs:
            max_eggs = orange_eggs
            name_max_eggs = "orange"

    elif colour_eggs == "blue":
        blue_eggs += 1
        if blue_eggs > max_eggs:
            max_eggs = blue_eggs
            name_max_eggs = "blue"
    elif colour_eggs == "green":
        green_eggs += 1
        if green_eggs > max_eggs:
            max_eggs = green_eggs
            name_max_eggs = "green"
    counter_eggs += 1

print(f"Red eggs: {red_eggs}")
print(f"Orange eggs: {orange_eggs}")
print(f"Blue eggs: {blue_eggs}")
print(f"Green eggs: {green_eggs}")
print(f"Max eggs: {max_eggs} -> {name_max_eggs}")
