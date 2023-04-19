num = int(input())

for numbers in range(1111, 10000):
    for digit in str(numbers):
        if digit == "0":
            break
        if num % int(digit) != 0:
            break
    else:
        print(numbers, end=" ")
