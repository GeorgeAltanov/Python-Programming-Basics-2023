paper = int(input())
cloth = int(input())
glue = float(input())
discount = int(input())

PAPER_PRICE = 5.80
CLOTH_PRICE = 7.20
GLUE_PRICE = 1.20

pape_price = paper * PAPER_PRICE
cloth_price = cloth * CLOTH_PRICE
glue_price = glue * GLUE_PRICE

total_price = pape_price + cloth_price + glue_price
total_price = total_price - (total_price * discount / 100)

print(f"{total_price:.3f}")
