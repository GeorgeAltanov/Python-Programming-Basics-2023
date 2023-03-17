budget = float(input())
destination = input()
season = input()
days = int(input())

total_price = 0

if season == "Winter":
    if destination == "Dubai":
        total_price = days * 45000 * 0.70
    elif destination == "Sofia":
        total_price = days * 17000 * 1.25
    elif destination == "London":
        total_price = days * 24000

elif season == "Summer":
    if destination == "Dubai":
        total_price = days * 40000 * 0.70
    elif destination == "Sofia":
        total_price = days * 12500 * 1.25
    elif destination == "London":
        total_price = days * 20250

if budget >= total_price:
    print(f"The budget for the movie is enough! We have {budget - total_price:.2f} leva left!")

else:
    print(f"The director needs {total_price - budget:.2f} leva more!")
