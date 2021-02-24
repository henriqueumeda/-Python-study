import string
print(string.ascii_lowercase)

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    letters_not_guessed = []
    for letter in string.ascii_lowercase:
        letters_not_guessed.append(letter)

    for letter in lettersGuessed:
        if letter in letters_not_guessed:
            letters_not_guessed.remove(letter)

    available_letters = ''.join(letters_not_guessed)
    return available_letters

lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
print(getAvailableLetters(lettersGuessed))
