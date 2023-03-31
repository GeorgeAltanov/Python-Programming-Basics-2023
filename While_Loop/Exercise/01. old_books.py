book = input()

counter = 0
input_book = None

while input_book != "No More Books":
    input_book = input()
    if input_book == "No More Books":
        print("The book you search is not here!")
        print(f"You checked {counter} books.")
        break

    if input_book == book:
        print(f"You checked {counter} books and found it.")
        break
    counter += 1
