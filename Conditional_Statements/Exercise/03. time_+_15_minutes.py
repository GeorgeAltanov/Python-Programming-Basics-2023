hours = int(input())
minutes = int(input())

minutes_total = minutes + 15
hours_time = hours + minutes_total // 60
minutes_time = minutes_total % 60

if hours_time > 23:
    hours_time = 0

print(f"{hours_time}:{minutes_time:02d}")
