years = int(input())
washing_machine_price = float(input())
toys_price = int(input())

birthdays_money = 0
money_from_gifts = 0
taken_from_brothers = 1

for age in range(1, years + 1):
    if age % 2 == 0:
        birthdays_money += 10
        money_from_gifts += birthdays_money - taken_from_brothers
    else:
        money_from_gifts += toys_price

if money_from_gifts >= washing_machine_price:
    print(f'Yes! {money_from_gifts -washing_machine_price:.2f}')
else:
    print(f'No! {washing_machine_price - money_from_gifts:.2f}')
