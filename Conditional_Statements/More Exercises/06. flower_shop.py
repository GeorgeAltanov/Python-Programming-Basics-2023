from math import ceil
from math import floor

MAGNOLIAS = 3.25
HYACINTHS = 4.00
ROSE = 3.50
CACTUS = 8.00

magnolias_count = int(input())
hyacinths_count = int(input())
rose_count = int(input())
cactus_count = int(input())
gift_price = float(input())

total_sum = magnolias_count * MAGNOLIAS + hyacinths_count * HYACINTHS + rose_count * ROSE + cactus_count * CACTUS
sum_after_fee = total_sum * 0.95

if sum_after_fee >= gift_price:
    print(f"She is left with {floor(sum_after_fee - gift_price)} leva.")
else:
    print(f"She will have to borrow {ceil(gift_price - sum_after_fee)} leva.")
