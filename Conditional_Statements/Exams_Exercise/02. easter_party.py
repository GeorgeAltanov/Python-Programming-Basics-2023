guests = int(input())
price_per_guest = float(input())
budget = float(input())

price_tort = budget * 0.10

if 10 <= guests <= 15:
    price_per_guest *= 0.85
elif 15 < guests <= 20:
    price_per_guest *= 0.80
elif guests > 20:
    price_per_guest *= 0.75

total_sum_party = guests * price_per_guest + price_tort

if budget >= total_sum_party:
    print(f"It is party time! {budget - total_sum_party:.2f} leva left.")
else:
    print(f"No party! {total_sum_party - budget:.2f} leva needed.")
