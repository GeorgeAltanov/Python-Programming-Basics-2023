size_eggs = input()
color_eggs = input()
count = int(input())
price = 0

if size_eggs == "Large":
    if color_eggs == "Red":
        price = 16
    elif color_eggs == "Green":
        price = 12
    elif color_eggs == "Yellow":
        price = 9
elif size_eggs == "Medium":
    if color_eggs == "Red":
        price = 13
    elif color_eggs == "Green":
        price = 9
    elif color_eggs == "Yellow":
        price = 7
elif size_eggs == "Small":
    if color_eggs == "Red":
        price = 9
    elif color_eggs == "Green":
        price = 8
    elif color_eggs == "Yellow":
        price = 5

total_price = count * price
expenses = total_price * 0.35
total_sum = total_price - expenses

print(f"{total_sum:.2f} leva.")
