num = int(input())

max_num = float("-inf")
sum_numbers = 0

for _ in range(num):
    current_number = int(input())
    if current_number > max_num:
        max_num = current_number
    sum_numbers += current_number

if max_num == sum_numbers - max_num:
    print(f"Yes\nSum = {max_num}")

else:
    sum_numbers = sum_numbers - max_num
    print(f"No\nDiff = {abs(max_num - sum_numbers)}")
