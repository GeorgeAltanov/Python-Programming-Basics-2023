eggs_count = int(input())

buy_eggs = 0
sold_eggs = 0

while True:
    command = input()
    if command == "Close":
        print("Store is closed!")
        print(f"{buy_eggs} eggs sold.")
        break
    eggs_buy_fill = int(input())


    if command == "Fill":
        eggs_count += eggs_buy_fill
        sold_eggs += eggs_buy_fill
    elif eggs_buy_fill > eggs_count:
        print(f"Not enough eggs in store!")
        print(f"You can buy only {eggs_count}.")
        break
    elif command == "Buy":
        eggs_count -= eggs_buy_fill
        buy_eggs += eggs_buy_fill
