text = ""
secret_command_c = False
secret_command_o = False
secret_command_n = False
counter_c = 0
counter_o = 0
counter_n = 0

while True:
    symbol = input()
    if secret_command_c == True  and secret_command_o == True and secret_command_n == True:
        secret_command_c, secret_command_o, secret_command_n = False, False, False
        counter_c, counter_o, counter_n = 0, 0, 0
        print(text,end=" ")
        text = ""

    if symbol == "End":
        break

    if (65 <= ord(symbol) <= 90) or (97 <= ord(symbol) <= 122):
        if symbol == "c":
            secret_command_c = True
            counter_c += 1
            if counter_c >= 2:
                text += "c"
            continue
        elif symbol == "o":
            secret_command_o = True
            counter_o += 1
            if counter_o >= 2:
                text += "o"
            continue
        elif symbol == "n":
            secret_command_n = True
            counter_n += 1
            if counter_n >= 2:
                text += "n"
            continue

        text += symbol
