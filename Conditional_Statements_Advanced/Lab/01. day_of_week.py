num = int(input())

day_of_week = None

if num == 1:
    day_of_week = "Monday"

elif num == 2:
    day_of_week = "Tuesday"

elif num == 3:
    day_of_week = "Wednesday"

elif num == 4:
    day_of_week = "Thursday"

elif num == 5:
    day_of_week = "Friday"

elif num == 6:
    day_of_week = "Saturday"

elif num == 7:
    day_of_week = "Sunday"

else:
    day_of_week = "Error"

print(day_of_week)
