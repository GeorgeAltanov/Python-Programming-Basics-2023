budget = float(input())
category = input()
peoples_in_group = int(input())

VIP = 499.99
NORMAL = 249.99

ticket_price = 0
transport = 0

if 1 <= peoples_in_group < 5:
    transport = budget * 0.75
elif peoples_in_group < 10:
    transport = budget * 0.60
elif peoples_in_group < 25:
    transport = budget * 0.50
elif peoples_in_group < 50:
    transport = budget * 0.40
else:
    transport = budget * 0.25
money_left_for_tickets = budget - transport

if category == "VIP":
    ticket_price = VIP * peoples_in_group
else:
    ticket_price = NORMAL * peoples_in_group

if money_left_for_tickets <= ticket_price:
    print(f"Not enough money! You need {ticket_price - money_left_for_tickets:.2f} leva.")
else:
    print(f"Yes! You have {money_left_for_tickets - ticket_price:.2f} leva left.")
