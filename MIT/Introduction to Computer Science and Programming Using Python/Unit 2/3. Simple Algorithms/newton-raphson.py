number = float(input('Input a number: '))

epsilon = 0.01
guess = number/2
num_guesses = 0

while abs(guess**2 - number) >= epsilon:
    num_guesses += 1
    guess -= (((guess**2) - number)/(2*guess))

print(f'Number of guesses: {num_guesses}')
print(f'Square root of {number} is about {guess}')
