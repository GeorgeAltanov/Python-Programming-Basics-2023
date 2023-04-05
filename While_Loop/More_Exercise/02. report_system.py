money_needed = int(input())

money_from_sales = 0
cash_payment = 0
credit_card_payment = 0

counter = 0
cash_payment_counter = 0
credit_card_payment_counter = 0

while money_from_sales < money_needed :
    price_of_product = input()
    counter += 1

    if price_of_product == "End":
        print(f"Failed to collect required money for charity.")
        break

    price_of_product = int(price_of_product)

    if counter % 2 == 1:
        if price_of_product <= 100:
            cash_payment += price_of_product
            money_from_sales += price_of_product
            cash_payment_counter += 1
            print("Product sold!")
        else:
            print("Error in transaction!")

    else:
        if price_of_product >= 10:
            credit_card_payment += price_of_product
            money_from_sales += price_of_product
            credit_card_payment_counter += 1
            print("Product sold!")

        else:
            print("Error in transaction!")

if money_from_sales >= money_needed:

    print(f"Average CS: {cash_payment / cash_payment_counter:.2f}")
    print(f"Average CC: {credit_card_payment / credit_card_payment_counter:.2f}")
