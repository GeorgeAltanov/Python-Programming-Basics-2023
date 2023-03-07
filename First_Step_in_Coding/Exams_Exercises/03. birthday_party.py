rent_for_the_hall = float(input())

tort_price = rent_for_the_hall * 0.20
drinks_price = tort_price * 0.55
animator_price = rent_for_the_hall / 3
total_price = rent_for_the_hall + tort_price + drinks_price + animator_price

print(total_price)
