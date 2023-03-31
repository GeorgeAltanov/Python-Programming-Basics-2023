balance = int(float(input()) * 100)
coins_counter = 0

while balance > 0:
    if balance >= 200:
        balance -= 200
    elif balance >= 100:
        balance -= 100
    elif balance >= 50:
        balance -= 50
    elif balance >= 20:
        balance -= 20
    elif balance >= 10:
        balance -= 10
    elif balance >= 5:
        balance -= 5
    elif balance >= 2:
        balance -= 2
    elif balance >= 1:
        balance -= 1
    coins_counter += 1

print(coins_counter)
