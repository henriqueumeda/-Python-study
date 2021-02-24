# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()


def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    for letter in secretWord:
        if letter not in lettersGuessed:
            return False
    return True


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    word_returned = ''
    for letter in secretWord:
        if letter not in lettersGuessed:
            word_returned += '_ '
        else:
            word_returned += letter

    return word_returned


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
    

def isLetterAvailable(lettersGuessed, user_letter):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if the letter isn't in lettersGuessed;
      False otherwise
    '''
    if user_letter not in lettersGuessed:
        return True
    return False


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


def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    mistakesMade = 0
    userWin = False
    lettersGuessed = []
    print('Welcome to the game Hangman!')
    print('I am thinking of a word that is {} letters long.'.format(len(secretWord)))
    while mistakesMade < 8 and userWin == False:
        print('-' * 13)
        print('You have {} guesses left.'.format(8-mistakesMade))
        print('Available letters: {}'.format(getAvailableLetters(lettersGuessed)))
        user_letter = input('Please guess a letter: ').lower()[0]
        if isLetterAvailable(lettersGuessed, user_letter) == True:
            lettersGuessed.append(user_letter)
            if isLetterInWord(user_letter, secretWord) == True:
                print('Good guess: ', end='')
            else:
                print('Oops! That letter is not in my word: ', end='')
                mistakesMade += 1
        else:
            print("Oops! You've already guessed that letter: ", end='')
        print(getGuessedWord(secretWord, lettersGuessed))
        userWin = isWordGuessed(secretWord, lettersGuessed)
    print('-' * 13)
    if userWin == True:
        print('Congratulations, you won!')
    else:
        print('Sorry, you ran out of guesses. The word was {}.'.format(secretWord))


# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
