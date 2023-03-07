mackerel_price = float(input())
sprinkle_price = float(input())
bonito_weight = float(input())
scad_weight = float(input())
midi_weight = float(input())

bonito_price = mackerel_price + mackerel_price * 0.60
scad_price = sprinkle_price + sprinkle_price * 0.80
midi_price = 7.50

total_price = bonito_price * bonito_weight + scad_price * scad_weight + midi_price * midi_weight

print(f"{total_price:.2f}")
