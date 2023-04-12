number = int(input())

valid_combinations_counter = 0

for x1 in range(26):
    for x2 in range(26):
        for x3 in range(26):
            valid_combinations = x1 + x2 + x3
            if valid_combinations == number:
                valid_combinations_counter += 1
print(valid_combinations_counter)
