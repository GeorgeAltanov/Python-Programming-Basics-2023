weekend = int(input())

NORM_FOR_PLAYS = 30000

weekend_time = weekend * 127
works_days = (365 - weekend) * 63
total_plays_time = weekend_time + works_days
time_more_for_plays = abs(total_plays_time - NORM_FOR_PLAYS)
h = time_more_for_plays // 60
minutes = time_more_for_plays % 60

if total_plays_time > NORM_FOR_PLAYS:
    print("Tom will run away")
    print(f"{h} hours and {minutes} minutes more for play")

else:
    print("Tom sleeps well")
    print(f"{h} hours and {minutes} minutes less for play")
