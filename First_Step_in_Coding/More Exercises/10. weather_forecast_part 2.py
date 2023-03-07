degrees = float(input())

weather = 0

if 26 <= degrees <= 35:
    weather = "Hot"
elif 20 < degrees < 26:
    weather = "Warm"
elif 15 <= degrees <= 20:
    weather = "Mild"
elif 12 <= degrees < 15:
    weather = "Cool"
elif 5 <= degrees < 12:
    weather = "Cold"

else:
    weather = "unknown"

print(weather)
