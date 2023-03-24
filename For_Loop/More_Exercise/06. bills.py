month = int(input())

total_bill_electricity = 0
water_bill = 20
internet_bill = 15
other_bills = 0
bill = 0

for _ in range(month):
    bill = float(input())
    total_bill_electricity += bill
    other_bills += (bill + water_bill + internet_bill) * 1.20

water_bill *= month
internet_bill *= month
average_bills = (total_bill_electricity + water_bill + internet_bill + other_bills) / month

print(f"Electricity: {total_bill_electricity:.2f} lv")
print(f"Water: {water_bill:.2f} lv")
print(f"Internet: {internet_bill:.2f} lv")
print(f"Other: {other_bills:.2f} lv")
print(f"Average: {average_bills:.2f} lv")
