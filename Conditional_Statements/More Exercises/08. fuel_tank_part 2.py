fuel = input()
fuel_count = float(input())
discount_card = input()

GASOLINE = 2.22
DIESEL = 2.33
GAS = 0.93

total_price = 0

if fuel == "Gasoline":
    total_price = fuel_count * GASOLINE
    if discount_card == "Yes":
        total_price = fuel_count * (GASOLINE - 0.18)
    if 20 <= fuel_count <= 25:
        total_price *= 0.92
    if fuel_count > 25:
        total_price *= 0.90
elif fuel == "Diesel":
    total_price = fuel_count * DIESEL
    if discount_card == "Yes":
        total_price = fuel_count * (DIESEL - 0.12)
    if 20 <= fuel_count <= 25:
        total_price *= 0.92
    if fuel_count > 25:
        total_price *= 0.90
elif fuel == "Gas":
    total_price = fuel_count * GAS
    if discount_card == "Yes":
        total_price = fuel_count * (GAS - 0.08)
    if 20 <= fuel_count <= 25:
        total_price *= 0.92
    if fuel_count > 25:
        total_price *= 0.90

print(f"{total_price:.2f} lv.")
