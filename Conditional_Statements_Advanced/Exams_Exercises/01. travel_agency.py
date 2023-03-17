city = input()
packet = input()
vip_discount = input()
days = int(input())

total_price = 0

if days > 7:
    days -= 1

if city == "Bansko" or city == "Borovets":
    if packet == "withEquipment":
        total_price = days * 100
        if vip_discount == "yes":
            total_price *= 0.90
    elif packet == "noEquipment":
        total_price = days * 80
        if vip_discount == "yes":
            total_price *= 0.95

elif city == "Varna" or city == "Burgas":
    if packet == "withBreakfast":
        total_price = days * 130
        if vip_discount == "yes":
            total_price *= 0.88
    elif packet == "noBreakfast":
        total_price = days * 100
        if vip_discount == "yes":
            total_price *= 0.93

if days < 1:
    print("Days must be positive number!")
elif (city == "Bansko" or city == "Borovets" or city == "Varna" or city == "Burgas") \
         and (packet == "noEquipment" or packet == "withEquipment" or packet == "noBreakfast" or packet == "withBreakfast"):
    print(f'The price is {total_price:.2f}lv! Have a nice time!')
else:
    print("Invalid input!")
