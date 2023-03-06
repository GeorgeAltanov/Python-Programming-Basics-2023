number_of_pages = int(input())
pages_for_one_hour = int(input())
number_of_days = int(input())

time = number_of_pages // pages_for_one_hour
hours_of_day = time // number_of_days

print(hours_of_day)
