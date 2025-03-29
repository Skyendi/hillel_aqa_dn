while True:
    word = input("Please enter a word with 'h' or 'H': ")
    if "h" in word or "H" in word:
        print("The letter 'h' or 'H' present in the word!")
        break
    else:
        print("Try again")