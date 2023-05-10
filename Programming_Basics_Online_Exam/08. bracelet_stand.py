budget = float(input())
money_sales = float(input())
expenses = float(input())
gift_price = float(input())

DAYS = 5

saved_money = DAYS * budget
win_money = DAYS * money_sales
total_saved_money = saved_money + win_money
total_saved_money -= expenses

if total_saved_money >= gift_price:
    print(f"Profit: {total_saved_money:.2f} BGN, the gift has been purchased.")
else:
    print(f"Insufficient money: {gift_price - total_saved_money:.2f} BGN.")
