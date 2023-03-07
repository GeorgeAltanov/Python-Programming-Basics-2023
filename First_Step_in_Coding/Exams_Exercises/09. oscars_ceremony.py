hall_rent = int(input())

statuettes_price = hall_rent - hall_rent * 0.30
catering_price = statuettes_price - statuettes_price * 0.15
voiceover_price = catering_price / 2

total_expenses = hall_rent + statuettes_price + catering_price + voiceover_price

print(f"{total_expenses:.2f}")
