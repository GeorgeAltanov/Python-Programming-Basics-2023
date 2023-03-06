yearly_fee = int(input())

shoes_price = yearly_fee - (yearly_fee * 0.40)
cloths_price = shoes_price - (shoes_price * 0.20)
ball_price = cloths_price / 4
accessories_price = ball_price / 5

total_price = yearly_fee + shoes_price + cloths_price + ball_price + accessories_price

print(total_price)
