num = int(input())

value = None

if num == 0:
    value = "No"
elif -100 <= num <= 100:
    value = "Yes"
else:
    value = "No"

print(value)
