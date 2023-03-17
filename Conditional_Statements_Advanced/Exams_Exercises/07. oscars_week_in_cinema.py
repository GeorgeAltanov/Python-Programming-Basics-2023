movie = input()
hall = input()
tickets_count = int(input())

total_tickets_price = 0

if movie == "A Star Is Born":
    if hall == "normal":
        total_tickets_price = tickets_count * 7.50
    elif hall == "luxury":
        total_tickets_price = tickets_count * 10.50
    elif hall == "ultra luxury":
        total_tickets_price = tickets_count * 13.50

elif movie == "Bohemian Rhapsody":
    if hall == "normal":
        total_tickets_price = tickets_count * 7.35
    elif hall == "luxury":
        total_tickets_price = tickets_count * 9.45
    elif hall == "ultra luxury":
        total_tickets_price = tickets_count * 12.75
elif movie == "Green Book":
    if hall == "normal":
        total_tickets_price = tickets_count * 8.15
    elif hall == "luxury":
        total_tickets_price = tickets_count * 10.25
    elif hall == "ultra luxury":
        total_tickets_price = tickets_count * 13.25
elif movie == "The Favourite":
    if hall == "normal":
        total_tickets_price = tickets_count * 8.75
    elif hall == "luxury":
        total_tickets_price = tickets_count * 11.55
    elif hall == "ultra luxury":
        total_tickets_price = tickets_count * 13.95

print(f"{movie} -> {total_tickets_price:.2f} lv.")
