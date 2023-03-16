season = input()
group = input()
students = int(input())
night = int(input())

sport = None
total_price = 0

if season == "Winter":
    if group == "girls":
        total_price = students * night * 9.60
        sport = "Gymnastics"
    elif group == "boys":
        total_price = students * night * 9.60
        sport = "Judo"
    elif group == "mixed":
        total_price = students * night * 10.00
        sport = "Ski"
elif season == "Spring":
    if group == "girls":
        total_price = students * night * 7.20
        sport = "Athletics"
    elif group == "boys":
        total_price = students * night * 7.20
        sport = "Tennis"
    elif group == "mixed":
        total_price = students * night * 9.50
        sport = "Cycling"
elif season == "Summer":
    if group == "girls":
        total_price = students * night * 15.00
        sport = "Volleyball"
    elif group == "boys":
        total_price = students * night * 15.00
        sport = "Football"
    elif group == "mixed":
        total_price = students * night * 20.00
        sport = "Swimming"

if students >= 50:
    total_price *= 0.50
if 20 <= students < 50:
    total_price *= 0.85
if 10 <= students < 20:
    total_price *= 0.95

print(f"{sport} {total_price:.2f} lv.")
