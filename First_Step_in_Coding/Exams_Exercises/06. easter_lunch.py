easter_bread = int(input())
crust_with_eggs = int(input())
cookies = int(input())

easter_bread_price = easter_bread * 3.20
crust_with_eggs_price = crust_with_eggs * 4.35
cookies_price = cookies * 5.40
paint_for_eggs = crust_with_eggs * 12 * 0.15

total_price = easter_bread_price + crust_with_eggs_price + cookies_price + paint_for_eggs

print(f"{total_price:.2f}")
