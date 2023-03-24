move = int(input())

result = 0
num_from_0_to_9 = 0
num_from_10_to_19 = 0
num_from_20_to_29 = 0
num_from_30_to_39 = 0
num_from_40_to_50 = 0
rest_num = 0

for _ in range(move):
    numbers = int(input())
    if 0 <= numbers <= 9:
        result += numbers * 0.20
        num_from_0_to_9 += 1
    elif 10 <= numbers <= 19:
        result += numbers * 0.30
        num_from_10_to_19 += 1
    elif 20 <= numbers <= 29:
        result += numbers * 0.40
        num_from_20_to_29 += 1
    elif 30 <= numbers <= 39:
        result += 50
        num_from_30_to_39 += 1
    elif 40 <= numbers <= 50:
        result += 100
        num_from_40_to_50 += 1
    else:
        result /= 2
        rest_num += 1

print(f"{result:.2f}")
print(f"From 0 to 9: {num_from_0_to_9 / move * 100:.2f}%")
print(f"From 10 to 19: {num_from_10_to_19 / move * 100:.2f}%")
print(f"From 20 to 29: {num_from_20_to_29 / move * 100:.2f}%")
print(f"From 30 to 39: {num_from_30_to_39 / move * 100:.2f}%")
print(f"From 40 to 50: {num_from_40_to_50 / move * 100:.2f}%")
print(f"Invalid numbers: {rest_num / move * 100:.2f}%")
