group_climbers = int(input())

musalla_person, mont_blanc_person, kilimanjaro_person, k2_person, everest_person = 0, 0, 0, 0, 0

for _ in range(group_climbers):
    person_count = int(input())

    if person_count <= 5:
        musalla_person += person_count
    elif person_count <= 12:
        mont_blanc_person += person_count
    elif person_count <= 25:
        kilimanjaro_person += person_count
    elif person_count <= 40:
        k2_person += person_count
    else:
        everest_person += person_count
total_person = musalla_person + mont_blanc_person + kilimanjaro_person + k2_person + everest_person

print(f"{musalla_person / total_person * 100:.2f}%")
print(f"{mont_blanc_person / total_person * 100:.2f}%")
print(f"{kilimanjaro_person / total_person * 100:.2f}%")
print(f"{k2_person / total_person * 100:.2f}%")
print(f"{everest_person / total_person * 100:.2f}%")
