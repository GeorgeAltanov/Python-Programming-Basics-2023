num = 0

while num >= 0:
    num = float(input())
    result = num * 2
    if result >= 0:
        print(f"Result: {result:.2f}")
else:
    print("Negative number!")
