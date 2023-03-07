airlines = input()
adults_tickets = int(input())
kids_tickets = int(input())
adults_tickets_price = float(input())
service_fee = float(input())

kids_tickets_price_plus_fee = adults_tickets_price * 0.30 + service_fee
adults_tickets_price_plus_fee = adults_tickets_price + service_fee

total_price = kids_tickets * kids_tickets_price_plus_fee + adults_tickets * adults_tickets_price_plus_fee
profit = total_price * 0.20

print(f"The profit of your agency from {airlines} tickets is {profit:.2f} lv.")
