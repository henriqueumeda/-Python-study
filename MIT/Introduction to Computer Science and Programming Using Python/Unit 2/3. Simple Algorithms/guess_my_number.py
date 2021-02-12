print('Please think of a number between 0 and 100!')
high = 100
low = 0
while True:
    guess = int((high + low) / 2)
    while True:
        answer = str(input("""Is your secret number {}?
Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.""".format(guess))).strip().lower()
        if answer != 'c' and answer != 'l' and answer != 'h':
            print("Sorry, I did not understand your input.")
        else:
            break
    if answer == 'c':
        break
    elif answer == 'l':
        low = guess
    else:
        high = guess

print('Game over. Your secret number was: {}'.format(guess))
