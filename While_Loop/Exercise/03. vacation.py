vacation_price = float(input())
balance = float(input())

days_spending = 0
total_days = 0

while days_spending < 5:
    action = input()
    money = float(input())

    total_days += 1

    if action == "spend":
        balance = balance - money if balance > money else 0
        days_spending += 1
    else:
        balance += money
        days_spending = 0

    if balance >= vacation_price:
        print(f"You saved the money for {total_days} days.")
        break
else:
    print("You can't save the money.")
    print(total_days)
