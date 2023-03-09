number = int(input())

bonus_score = 0

if number <= 100:
    bonus_score = 5
elif 100 < number < 1000:
    bonus_score = number * 0.20
else:
    bonus_score = number * 0.10

if number % 2 == 0:
    bonus_score += 1

elif number % 10 == 5:
    bonus_score += 2

print(bonus_score)
print(bonus_score + number)
