term_of_contract = input()
contract = input()
internet = input()
month_pay = int(input())

price = 0

if term_of_contract == "one":
    if contract == "Small":
        price = 9.98
    elif contract == "Middle":
        price = 18.99
    elif contract == "Large":
        price = 25.98
    elif contract == "ExtraLarge":
        price = 35.99

elif term_of_contract == "two":
    if contract == "Small":
        price = 8.58
    elif contract == "Middle":
        price = 17.09
    elif contract == "Large":
        price = 23.59
    elif contract == "ExtraLarge":
        price = 31.79

if internet == "yes":
    if price <= 10:
        price += 5.50
    elif price <= 30:
        price += 4.35
    elif price > 30:
        price += 3.85

price *= month_pay

if term_of_contract == "two":
    price *= 0.9625

print(f"{price:.2f} lv.")
