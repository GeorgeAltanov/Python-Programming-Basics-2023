chicken_menu = int(input())
fish_menu = int(input())
vegan_menu = int(input())

CHICKEN_PRICE = 10.35
FISH_PRICE = 12.40
VEGETARIAN_PRICE = 8.15
DELIVERY = 2.50

price_menus = chicken_menu * CHICKEN_PRICE + fish_menu * FISH_PRICE + vegan_menu * VEGETARIAN_PRICE
price_deserts = price_menus * 0.20
price_delivery = 2.50

total_price = price_menus + price_deserts + price_delivery

print(f"{total_price:.2f}")
