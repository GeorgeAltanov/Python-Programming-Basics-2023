fuel = input()
fuel = fuel.lower()
litres_of_fuel = float(input())

if fuel == "diesel" or fuel == "gasoline" or fuel == "gas":
    if litres_of_fuel >= 25:
        print(f"You have enough {fuel}.")
    else:
        print(f"Fill your tank with {fuel}!")
        
else:
    print("Invalid fuel!")
