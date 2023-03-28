budget = float(input())

while True:
    actor = input()

    if actor == "ACTION":
        print(f"We are left with {budget:.2f} leva.")
        break

    if len(actor) <= 15:
        honorarium = float(input())

    else:
        honorarium = budget * 0.20

    budget -= honorarium

    if budget < 0:
        print(f"We need {abs(budget):.2f} leva for our actors.")
        break
