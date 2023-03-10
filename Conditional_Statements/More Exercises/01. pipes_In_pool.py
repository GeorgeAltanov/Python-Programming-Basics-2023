from math import ceil

series_name = input()
episode_time = int(input())
break_time = int(input())

lunch_time = break_time / 8
relax_time = break_time / 4

time_taken = lunch_time + relax_time + episode_time
left_time = break_time - time_taken

if left_time >= 0:
    print(f"You have enough time to watch {series_name} and left with"
          f" {ceil(left_time)} minutes free time.")
else:
    print(f"You don't have enough time to watch {series_name}, you need {ceil(abs(left_time))} more minutes.")
