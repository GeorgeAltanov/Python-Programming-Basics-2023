cargo_count = int(input())

total_cargo_weight = 0

minibus_cargo = 0
track_cargo = 0
train_cargo = 0

MINIBUS_PRICE = 200
TRACK_PRICE = 175
TRAIN_PRICE = 120

for _ in range(cargo_count):
    cargo_weight = int(input())
    total_cargo_weight += cargo_weight
    if cargo_weight <= 3:
        minibus_cargo += cargo_weight
    elif cargo_weight <= 11:
        track_cargo += cargo_weight
    else:
        train_cargo += cargo_weight
price_per_ton = (minibus_cargo * MINIBUS_PRICE + track_cargo * TRACK_PRICE
                 + train_cargo * TRAIN_PRICE) / total_cargo_weight
minibus_price_per_ton = minibus_cargo / total_cargo_weight * 100
track_price_per_ton = track_cargo / total_cargo_weight * 100
train_price_per_ton = train_cargo / total_cargo_weight * 100

print(f"{price_per_ton:.2f}")
print(f"{minibus_price_per_ton:.2f}%")
print(f"{track_price_per_ton:.2f}%")
print(f"{train_price_per_ton:.2f}%")
