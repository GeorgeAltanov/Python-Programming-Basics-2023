exam_hour = int(input())
exam_minutes = int(input())
student_hour = int(input())
student_minutes = int(input())

exam_time_in_minutes = exam_hour * 60 + exam_minutes
student_time_in_minutes = student_hour * 60 + student_minutes
time_diff = exam_time_in_minutes - student_time_in_minutes

if time_diff > 30:
    print("Early")
elif time_diff < 0:
    print("Late")
else:
    print("On time")

hours = 0
minutes = abs(time_diff)

result = ""

if minutes >= 60:
    hours = minutes // 60
    minutes = minutes % 60

if hours > 0:
    result = f"{hours}:{minutes:02d} hours"

elif minutes > 0:
    result = f"{minutes} minutes"

if time_diff > 0:
    result += " before the start"
elif time_diff < 0:
    result += " after the start"

print(result)
