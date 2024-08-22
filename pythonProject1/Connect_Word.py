word = ""
stop = False
while not stop:
    letter = input("Input a letter or 'stop' to stop: ").lower()
    if letter == "stop":
        do_play = True
        while do_play:
            yes_or_no = input("Play again? Yes or No!: ").lower()
            if yes_or_no == "yes":
                do_play = False
                stop = False
                word += " "
            else:
                stop = True
                do_play = False
    elif len(letter) > 1:
        print("too many. Try again")
        stop = False
    else:
        stop = False
        word += letter
print(word)
