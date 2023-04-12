floor = int(input())
flats_per_floor = int(input())

flat_name = ""

for current_floor in range(floor, 0, -1):
    for number in range(0, flats_per_floor):

        if current_floor == floor:
            flat_name = f"L{current_floor}{number}"
        elif current_floor % 2 == 0:
            flat_name = f"O{current_floor}{number}"
        elif current_floor % 2 == 1:
            flat_name = f"A{current_floor}{number}"
        print(flat_name, end=" ")
    print()
