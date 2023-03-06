nylon = int(input())
paint = int(input())
thinner = int(input())
work_hours = int(input())

NYLON_PRICE = 1.50
PAINT_PRICE = 14.50
THINNER_PRICE = 5
PACKETS_PRICE = 0.40

materials_price = (nylon + 2) * NYLON_PRICE + (paint + (paint * 0.10)) * PAINT_PRICE + \
                  thinner * THINNER_PRICE + PACKETS_PRICE
price_for_one_hour_of_work = (materials_price * 0.30) * work_hours
total_price = materials_price + price_for_one_hour_of_work

print(total_price)
