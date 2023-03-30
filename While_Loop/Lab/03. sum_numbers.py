num = int(input())

numbers_sum = 0

while True:
    numbers = int(input())
    numbers_sum += numbers
    if numbers_sum >= num:
        break
        
print(numbers_sum)
