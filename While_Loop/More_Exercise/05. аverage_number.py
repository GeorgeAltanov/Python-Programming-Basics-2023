num = int(input())

numbers_sum = 0
counter = 0

while True:
    numbers = int(input())
    numbers_sum += numbers
    counter += 1
    if counter >= num:
        print(f"{numbers_sum / num:.2f}")
        break
