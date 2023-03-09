budget = float(input())

graphic_cards_count = int(input())
processors_count = int(input())
ram_count = int(input())

GRAPHIC_CARD_PRICE_ONE = 250

graphic_card_price = graphic_cards_count * GRAPHIC_CARD_PRICE_ONE
processors_price = processors_count * graphic_card_price * 0.35
ram_price = ram_count * graphic_card_price * 0.10

total_price = graphic_card_price + processors_price + ram_price

if graphic_cards_count > processors_count:
    total_price *= 0.85

if total_price <= budget:
    print(f"You have {budget - total_price:.2f} leva left!")
else:
    print(f"Not enough money! You need {total_price - budget:.2f} leva more!")
