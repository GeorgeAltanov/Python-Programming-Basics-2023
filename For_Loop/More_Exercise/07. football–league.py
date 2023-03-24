capacity_of_stadium = int(input())
fans_count = int(input())

fans_in_sector_a = 0
fans_in_sector_b = 0
fans_in_sector_v = 0
fans_in_sector_g = 0

for _ in range(fans_count):
    sector = input()
    if sector == "A":
        fans_in_sector_a += 1
    elif sector == "B":
        fans_in_sector_b += 1
    elif sector == "V":
        fans_in_sector_v += 1
    elif sector == "G":
        fans_in_sector_g += 1

print(f"{fans_in_sector_a / fans_count * 100:.2f}%")
print(f"{fans_in_sector_b / fans_count * 100:.2f}%")
print(f"{fans_in_sector_v / fans_count * 100:.2f}%")
print(f"{fans_in_sector_g / fans_count * 100:.2f}%")
print(f"{fans_count / capacity_of_stadium * 100:.2f}%")
