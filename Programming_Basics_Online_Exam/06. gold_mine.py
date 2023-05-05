locations = int(input())

locations_counter = 0

while locations_counter < locations:

    expected_average_yield = float(input())
    days_dig = int(input())

    average_yield_gold = 0
    yield_gold = 0
    counter = 0

    for _ in range(days_dig):
        yield_gold_per_day = float(input())
        yield_gold += yield_gold_per_day

        counter += 1

        if counter == days_dig:
            break
    locations_counter += 1
    average_yield_gold = yield_gold / days_dig

    if average_yield_gold >= expected_average_yield:
        print(f"Good job! Average gold per day: {average_yield_gold:.2f}.")

    else:
        print(f"You need {expected_average_yield - average_yield_gold:.2f} gold.")
