amount_deposited = float(input())
month = int(input())
annual_interest_rate = float(input())

sum_rate = amount_deposited * annual_interest_rate / 100
sum_rate_month = sum_rate / 12
price = amount_deposited + (month * sum_rate_month)

print(price)
