def isLetterAvailable(lettersGuessed, user_letter):
    '''
    lettersGuessed: list, what letters have been guessed so far
    user_letter: letter guessed by user
    returns: boolean, True if the letter isn't in lettersGuessed;
      False otherwise
    '''
    if user_letter not in lettersGuessed:
        return True
    return False

lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
print(isLetterAvailable(lettersGuessed, 'e'))
