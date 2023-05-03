city, packet, vip_discount = input(), input(), input()
days = int(input())

days = days - 1 if days > 7 else days
total_price = 0

INVALID_INPUT = False
NEGATIVE_NUMBER = False

if days < 1:
    NEGATIVE_NUMBER = True

else:
    if city == "Bansko" or city == "Borovets":
        if packet == "withEquipment":
            total_price = days * 100
            if vip_discount == "yes":
                total_price *= 0.90
        elif packet == "noEquipment":
            total_price = days * 80
            if vip_discount == "yes":
                total_price *= 0.95
        else:
            INVALID_INPUT = True

    elif city == "Varna" or city == "Burgas":
        if packet == "withBreakfast":
            total_price = days * 130
            if vip_discount == "yes":
                total_price *= 0.88
        elif packet == "noBreakfast":
            total_price = days * 100
            if vip_discount == "yes":
                total_price *= 0.93
        else:
            INVALID_INPUT = True
    else:
        INVALID_INPUT = True

if NEGATIVE_NUMBER:
    print("Days must be positive number!")
elif INVALID_INPUT:
    print("Invalid input!")
else:
    print(f'The price is {total_price:.2f}lv! Have a nice time!')
