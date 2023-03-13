type_of_projection = input()
rows = int(input())
columns = int(input())

PREMIERE = 12.00
NORMAL = 7.50
DISCOUNT = 5.00

price = 0

if type_of_projection == "Premiere":
    price = rows * columns * PREMIERE
elif type_of_projection == "Normal":
    price = rows * columns * NORMAL
else:
    price = rows * columns * DISCOUNT

print(f"{price:.2f} leva")
