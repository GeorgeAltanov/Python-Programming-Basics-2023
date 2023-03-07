strawberries_price = float(input())
bananas_kg = float(input())
oranges_kg = float(input())
raspberries_kg = float(input())
strawberries_kg = float(input())

raspberries_price = strawberries_price / 2
oranges_price = raspberries_price - raspberries_price * 0.40
bananas_price = raspberries_price - raspberries_price * 0.80

total_price = raspberries_price * raspberries_kg + oranges_price * oranges_kg + \
              bananas_price * bananas_kg + strawberries_price * strawberries_kg

print(f"{total_price:.2f}")
