vegetables_price = float(input())
fruits_price = float(input())
vegetables_kg = int(input())
fruits_kg = int(input())

euro = 1.94

sum_vegetables_and_fruits = vegetables_price * vegetables_kg + fruits_price * fruits_kg
sum_in_euro = sum_vegetables_and_fruits / euro

print(f"{sum_in_euro:.2f}")
