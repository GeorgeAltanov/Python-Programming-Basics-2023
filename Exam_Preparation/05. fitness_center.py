visitors = int(input())

back, chest, legs, abs_training, protein_shake, protein_bar = 0, 0, 0, 0 ,0 ,0

for _ in range(visitors):
    activity = input()
    if activity == "Back":
        back += 1
    elif activity == "Chest":
        chest += 1
    elif activity == "Legs":
        legs += 1
    elif activity == "Abs":
        abs_training += 1
    elif activity == "Protein shake":
        protein_shake += 1
    elif activity == "Protein bar":
        protein_bar += 1

training_people = back + chest + legs + abs_training
people_buy = protein_shake + protein_bar

print(f"{back} - back")
print(f"{chest} - chest")
print(f"{legs} - legs")
print(f"{abs_training} - abs")
print(f"{protein_shake} - protein shake")
print(f"{protein_bar} - protein bar")
print(f"{training_people / visitors * 100:.2f}% - work out")
print(f"{people_buy / visitors * 100:.2f}% - protein")
