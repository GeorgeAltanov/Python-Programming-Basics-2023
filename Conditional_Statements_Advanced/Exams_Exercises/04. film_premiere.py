movie = input()
extras = input()
tickets_count = int(input())

total_price = 0

if movie == "John Wick":
    if extras == "Drink":
        total_price = tickets_count * 12
    elif extras == "Popcorn":
        total_price = tickets_count * 15
    elif extras == "Menu":
        total_price = tickets_count * 19

elif movie == "Star Wars":
    if extras == "Drink":
        total_price = tickets_count * 18
    elif extras == "Popcorn":
        total_price = tickets_count * 25
    elif extras == "Menu":
        total_price = tickets_count * 30
    if tickets_count >= 4:
        total_price *= 0.70

elif movie == "Jumanji":
    if extras == "Drink":
        total_price = tickets_count * 9
    elif extras == "Popcorn":
        total_price = tickets_count * 11
    elif extras == "Menu":
        total_price = tickets_count * 14
    if tickets_count == 2:
        total_price *= 0.85

print(f"Your bill is {total_price:.2f} leva.")
