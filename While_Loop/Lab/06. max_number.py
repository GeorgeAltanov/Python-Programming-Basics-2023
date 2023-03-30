max_number = float("-inf")

while True:
    num = input()
    if num == "Stop":
        break
    num = int(num)
    if num > max_number:
        max_number = num
        
print(max_number)
