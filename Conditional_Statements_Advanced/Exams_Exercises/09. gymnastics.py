country = input()
equipment = input()

total_grades = 0
percent_needed = 0

if equipment == "ribbon":
    if country == "Russia":
        total_grades = 9.100 + 9.400
        percent_needed = (20 - total_grades) / 20 * 100
    elif country == "Bulgaria":
        total_grades = 9.600 + 9.400
        percent_needed = (20 - total_grades) / 20 * 100
    elif country == "Italy":
        total_grades = 9.200 + 9.500
        percent_needed = (20 - total_grades) / 20 * 100

elif equipment == "hoop":
    if country == "Russia":
        total_grades = 9.300 + 9.800
        percent_needed = (20 - total_grades) / 20 * 100
    elif country == "Bulgaria":
        total_grades = 9.550 + 9.750
        percent_needed = (20 - total_grades) / 20 * 100
    elif country == "Italy":
        total_grades = 9.450 + 9.350
        percent_needed = (20 - total_grades) / 20 * 100

elif equipment == "rope":
    if country == "Russia":
        total_grades = 9.600 + 9.000
        percent_needed = (20 - total_grades) / 20 * 100
    elif country == "Bulgaria":
        total_grades = 9.500 + 9.400
        percent_needed = (20 - total_grades) / 20 * 100
    elif country == "Italy":
        total_grades = 9.700 + 9.150
        percent_needed = (20 - total_grades) / 20 * 100

print(f"The team of {country} get {total_grades:.3f} on {equipment}.")
print(f"{percent_needed:.2f}%")
