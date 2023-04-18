prime_number_sum,non_prime_number_sum = 0, 0

while True:
    command = input()
    is_prime = True

    if command == "stop":
        break
    current_number = int(command)

    if current_number < 0:
        print("Number is negative.")
        continue

    for number in range(2, current_number):
        if current_number % number == 0:
            is_prime = False
            break

    if is_prime:
        prime_number_sum += current_number

    else:
        non_prime_number_sum += current_number

print(f"Sum of all prime numbers is: {prime_number_sum}")
print(f"Sum of all non prime numbers is: {non_prime_number_sum}")
