from math import floor
from math import ceil

tennis_racket_price = float(input())
tennis_rackets = int(input())
sport_shoes = int(input())

rackets_price = tennis_racket_price * tennis_rackets
sport_shoes_price = (tennis_racket_price / 6) * sport_shoes
another_equipment = (rackets_price + sport_shoes_price) * 0.20

total_price = rackets_price + sport_shoes_price + another_equipment

price_for_djokovic = (floor(total_price / 8))
price_for_sponsor = (ceil(total_price * 7 / 8))

print(f"Price to be paid by Djokovic {price_for_djokovic}")
print(f"Price to be paid by sponsors {price_for_sponsor}")
