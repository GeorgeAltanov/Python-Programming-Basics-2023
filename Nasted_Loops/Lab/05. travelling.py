money_earned = 0

while True:
    destination = input()
    if destination == "End":
        break
    budget = input()
    budget = float(budget)
    while money_earned <= budget:
        money = float(input())
        money_earned += money
        if money_earned >= budget:
            print(f"Going to {destination}!")
            money_earned = 0
            break
