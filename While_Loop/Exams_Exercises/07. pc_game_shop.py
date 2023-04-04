games_sold = int(input())

hearthstone = 0
fornite = 0
overwatch = 0
others = 0
counter = 0

while counter < games_sold:
    name_game = input()
    if name_game == "Hearthstone":
        hearthstone += 1
    elif name_game == "Fornite":
        fornite += 1
    elif name_game == "Overwatch":
        overwatch += 1
    else:
        others += 1
    counter += 1

print(f"Hearthstone - {hearthstone / games_sold * 100:.2f}%")
print(f"Fornite - {fornite / games_sold * 100:.2f}%")
print(f"Overwatch - {overwatch / games_sold * 100:.2f}%")
print(f"Others - {others / games_sold * 100:.2f}%")
