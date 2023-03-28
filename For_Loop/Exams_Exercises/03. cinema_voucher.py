voucher = int(input())

ticket_count = 0
product_count = 0
price_ticket = 0
price_product = 0

while True:
    purchase = input()
    if purchase == "End":
        break

    if len(purchase) > 8:
        price_ticket = ord(purchase[0]) + ord(purchase[1])
        voucher -= price_ticket
        if voucher >= 0:
            ticket_count += 1
    elif len(purchase) <= 8:
        price_product = ord(purchase[0])
        voucher -= price_product
        if voucher >= 0:
            product_count += 1

    if voucher < 0:
        break

print(ticket_count)
print(product_count)
