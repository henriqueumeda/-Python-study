def isLetterInWord(user_letter, secretWord):
    '''
    user_letter: letter guessed by user
    secretWord: string, the word the user is guessing
    returns: boolean, True if the letter is in the secretWord;
      False otherwise
    '''
    secretWordList = []
    secretWordList[:0] = secretWord
    if user_letter in secretWordList:
        return True
    return False

print(isLetterInWord('e', 'ranch'))
