flour_kg_price = float(input())
flour_kg = float(input())
sugar_kg = float(input())
crust_with_eggs = int(input())
yeast_packets = int(input())

sugar_kg_price = (flour_kg_price - flour_kg_price * 0.25) * sugar_kg
crust_with_eggs_price = (flour_kg_price + flour_kg_price * 0.10) * crust_with_eggs
yeast_packets_price = (sugar_kg_price - sugar_kg_price * 0.80) / sugar_kg * yeast_packets
flour_price = flour_kg_price * flour_kg

total_price = sugar_kg_price + crust_with_eggs_price + yeast_packets_price + flour_price

print(f"{total_price:.2f}")
