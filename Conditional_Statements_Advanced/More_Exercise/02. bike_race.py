juniors_count = int(input())
seniors_count = int(input())
track_type = input()

total_sum = 0
juniors_taxes = 0
seniors_taxes = 0
expenses = 0.95
if track_type == "trail":
    juniors_taxes = 5.50
    seniors_taxes = 7.00
    total_sum = (juniors_count * juniors_taxes + seniors_count * seniors_taxes) * expenses

elif track_type == "cross-country":
    juniors_taxes = 8.00
    seniors_taxes = 9.50
    total_sum = (juniors_count * juniors_taxes + seniors_count * seniors_taxes) * expenses
    if juniors_count + seniors_count >= 50:
        total_sum *= 0.75
elif track_type == "downhill":
    juniors_taxes = 12.25
    seniors_taxes = 13.75
    total_sum = (juniors_count * juniors_taxes + seniors_count * seniors_taxes) * expenses
elif track_type == "road":
    juniors_taxes = 20.00
    seniors_taxes = 21.50
    total_sum = (juniors_count * juniors_taxes + seniors_count * seniors_taxes) * expenses

print(f"{total_sum:.2f}")
