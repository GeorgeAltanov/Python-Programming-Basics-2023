working_time = int(input())
day_of_week = input()

time_table = None

if day_of_week == "Sunday":
    time_table = "closed"

if day_of_week == "Monday" or day_of_week == "Tuesday" or day_of_week == "Wednesday" \
        or day_of_week == "Thursday" or day_of_week == "Friday" or day_of_week == "Saturday":
    if 10 <= working_time <= 18:
        time_table = "open"
    else:
        time_table = "closed"

print(time_table)
