legacy_money = float(input())
year_to_live = int(input())

YEARS_OF_IVAN = 18
expenses = 0

for year in range(1800, year_to_live + 1):
    YEARS_OF_IVAN += 1
    if year % 2 == 0:
        expenses += 12000
    else:
        expenses += 12000 + 50 * YEARS_OF_IVAN
    # YEARS_OF_IVAN += 1
if legacy_money >= expenses:
    print(f"Yes! He will live a carefree life and will have {legacy_money - expenses:.2f} dollars left.")
else:
    print(f"He will need {expenses - legacy_money:.2f} dollars to survive.")
