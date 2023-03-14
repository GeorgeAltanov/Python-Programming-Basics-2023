day_of_week = input()

part_of_week = None

if day_of_week == "Monday" or day_of_week == "Tuesday" or day_of_week == "Wednesday"\
        or day_of_week == "Thursday" or day_of_week == "Friday":
    part_of_week = "Working day"

elif day_of_week == "Saturday" or day_of_week == "Sunday":
    part_of_week = "Weekend"

else:
    part_of_week = "Error"

print(part_of_week)
