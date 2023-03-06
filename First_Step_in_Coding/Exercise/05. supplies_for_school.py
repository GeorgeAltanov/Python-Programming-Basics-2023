pens_packets = int(input())
marker_packets = int(input())
cleaning_detergent = int(input())
discount = int(input())

PEN_PRICE = 5.80
MARKER_PRICE = 7.20
DETERGENT_PRICE = 1.20

price_before_discount = pens_packets * PEN_PRICE + marker_packets * MARKER_PRICE + cleaning_detergent * DETERGENT_PRICE
total_price = price_before_discount - (price_before_discount * discount / 100)

print(f"{total_price:.2f}")
