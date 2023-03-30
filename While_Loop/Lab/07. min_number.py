min_number = float("inf")

while True:
    num = input()
    if num == "Stop":
        break
    num = int(num)
    if num < min_number:
        min_number = num
        
print(min_number)
