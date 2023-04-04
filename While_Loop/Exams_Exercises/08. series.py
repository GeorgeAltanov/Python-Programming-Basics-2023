budget = float(input())
movies_count = int(input())

total_price = 0

for _ in range(movies_count):
    name_of_movie = input()
    price_of_movie = float(input())

    if name_of_movie == "Thrones":
        price_of_movie *= 0.50
    elif name_of_movie == "Lucifer":
        price_of_movie *= 0.60
    elif name_of_movie == "Protector":
        price_of_movie *= 0.70
    elif name_of_movie == "TotalDrama":
        price_of_movie *= 0.80
    elif name_of_movie == "Area":
        price_of_movie *= 0.90

    else:
        price_of_movie = price_of_movie

    total_price += price_of_movie

if budget >= total_price:
    print(f"You bought all the series and left with {budget - total_price:.2f} lv.")
else:
    print(f"You need {total_price - budget:.2f} lv. more to buy the series!")
