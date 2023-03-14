product = input()

name_of_product = None

if product == "banana" or product == "apple" or product == "kiwi" \
        or product == "cherry" or product == "lemon" or product == "grapes":
    name_of_product = "fruit"
elif product == "tomato" or product == "cucumber" or product == "pepper" or product == "carrot":
    name_of_product = "vegetable"
else:
    name_of_product = "unknown"

print(name_of_product)
