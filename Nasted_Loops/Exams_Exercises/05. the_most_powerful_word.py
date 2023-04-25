from math import floor

word = None
first_char = None
max_points = 0
counter_char = 0
winner_word = None

while True:
    word = input()
    if word == "End of words":
        break

    length_word = len(word)
    points = 0
    first_char = None
    counter_char = 0

    for char in word:
        points += ord(char)
        counter_char += 1

        if counter_char == 1:
            first_char = char

    if first_char == "a" or first_char == "e" or first_char == "i" or first_char == "o" or first_char == "u"\
        or first_char == "y"or  first_char == "A" or first_char == "E" or first_char == "I" or first_char == "O"\
            or first_char == "U" or first_char == "Y":

        points *= length_word
    else:
        points /= length_word

    if points > max_points:
        max_points = points
        winner_word = word

print(f"The most powerful word is {winner_word} - {floor(max_points)}")
