age = float(input())
gender = input()

title = None

if age >= 16 and gender == "m":
    title = "Mr."

elif age < 16 and gender == "m":
    title = "Master"

elif age >= 16 and gender == "f":
    title = "Ms."
    
elif age < 16 and gender == "f":
    title = "Miss"

print(title)
