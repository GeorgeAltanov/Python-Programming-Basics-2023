from math import ceil

video_card_price = int(input())
switch_price = int(input())
electricity_price = float(input())
profit_per_day = float(input())

VIDEO_CARD = 13
SWITCH = 13
MONEY_SPENT = 1000

total_video_card_price = video_card_price * VIDEO_CARD
total_switch_price = switch_price * SWITCH
money_spent = total_video_card_price + total_switch_price + MONEY_SPENT
spent_from_card_for_day = profit_per_day - electricity_price
total_spent_per_day_for_card = VIDEO_CARD * spent_from_card_for_day
payout = money_spent / total_spent_per_day_for_card

print(money_spent)
print(f"{ceil(payout)}")
