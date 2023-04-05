n, c, o = 0, 0, 0
word = ""

while True:
    letter = input()
    if letter.isalpha():
        if letter == "End":
         break

        if letter == "n" and n == 0:
            n = 1
        elif letter == "c" and c == 0:
            c = 1
        elif letter == "o" and o == 0:
            o = 1
        else:
            word += letter

    if n == 1 and c == 1 and o == 1:
        n, c, o = 0, 0, 0
        print(word, end=" ")
        word = ""
