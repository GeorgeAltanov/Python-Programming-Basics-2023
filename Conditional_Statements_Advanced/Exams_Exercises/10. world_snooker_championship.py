stage = input()
ticket = input()
count_of_ticket = int(input())
foto = input()

total_price = 0

if ticket == "Standard":
    if stage == "Quarter final":
        total_price = count_of_ticket * 55.50
    elif stage == "Semi final":
        total_price = count_of_ticket * 75.88
    elif stage == "Final":
        total_price = count_of_ticket * 110.10

elif ticket == "Premium":
    if stage == "Quarter final":
        total_price = count_of_ticket * 105.20
    elif stage == "Semi final":
        total_price = count_of_ticket * 125.22
    elif stage == "Final":
        total_price = count_of_ticket * 160.66

elif ticket == "VIP":
    if stage == "Quarter final":
        total_price = count_of_ticket * 118.90
    elif stage == "Semi final":
        total_price = count_of_ticket * 300.40
    elif stage == "Final":
        total_price = count_of_ticket * 400.00

if total_price > 4000:
    total_price *= 0.75
elif 2500 < total_price <= 4000:
    total_price *= 0.90
    if foto == "Y":
        total_price += count_of_ticket * 40
    elif foto == "N":
        total_price = total_price
else:
    if foto == "Y":
        total_price += count_of_ticket * 40
    elif foto == "N":
        total_price = total_price

print(f"{total_price:.2f}")
