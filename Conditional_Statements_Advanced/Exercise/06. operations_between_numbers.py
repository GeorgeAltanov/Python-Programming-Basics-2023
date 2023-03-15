num_1 = int(input())
num_2 = int(input())
operator = input()

result = 0

if operator == "+":
    result = f"{num_1} + {num_2} = {num_1 + num_2}" + (" - even" if (num_1 + num_2) % 2 == 0 else " - odd")
elif operator == "-":
    result = f"{num_1} - {num_2} = {num_1 - num_2}" + (" - even" if (num_1 - num_2) % 2 == 0 else " - odd")
elif operator == "*":
    result = f"{num_1} * {num_2} = {num_1 * num_2}" + (" - even" if (num_1 * num_2) % 2 == 0 else " - odd")
elif num_2 == 0:
    result = f"Cannot divide {num_1} by zero"
elif operator == "%":
    result = f"{num_1} % {num_2} = {num_1 % num_2}"
elif operator == "/":
    result = f"{num_1} / {num_2} = {num_1 / num_2:.2f}"

print(result)
