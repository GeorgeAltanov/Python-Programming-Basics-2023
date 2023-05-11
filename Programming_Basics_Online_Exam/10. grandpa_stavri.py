days = int(input())

total_liter = 0
total_degrees = 0

for _ in range(days):
    liter = float(input())
    degrees = float(input())

    total_liter += liter
    degrees_per_liter = liter * degrees
    total_degrees += degrees_per_liter

total_degrees /= total_liter

print(f"Liter: {total_liter:.2f}")
print(f"Degrees: {total_degrees:.2f}")

if total_degrees < 38:
    print("Not good, you should baking!")
elif 38 <= total_degrees < 42:
    print("Super!")
else:
    print("Dilution with distilled water!")
