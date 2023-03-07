annual_fee_basketball = int(input())

shoes_basketball = annual_fee_basketball - annual_fee_basketball * 0.40
equipment = shoes_basketball - shoes_basketball * 0.20
ball_basketball = equipment / 4
accessories = ball_basketball / 5

total_fee = annual_fee_basketball + shoes_basketball + equipment + ball_basketball + accessories

print(f"{total_fee:.2f}")
