from ps4a import *

def playHand(hand, wordList, n):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    * The user may input a word or a single period (the string ".")
      to indicate they're done playing
    * Invalid words are rejected, and a message is displayed asking
      the user to choose another word until they enter a valid word or "."
    * When a valid word is entered, it uses up letters from the hand.
    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.
    * The sum of the word scores is displayed when the hand finishes.
    * The hand finishes when there are no more unused letters or the user
      inputs a "."

      hand: dictionary (string -> int)
      wordList: list of lowercase strings
      n: integer (HAND_SIZE; i.e., hand size required for additional points)

    """
    acumulated_points = 0
    number_of_remaining_letters = n
    while number_of_remaining_letters > 0:
        print('Current hand: ', end='')
        displayHand(hand)
        word = input('Enter word, or a "." to indicate that you are finished: ')
        if isValidWord(word, hand, wordList) == True:
            word_points = getWordScore(word, n)
            acumulated_points += word_points
            print('"{}" earned {}. Total: {} points\n'.format(word, word_points, acumulated_points))
            hand = updateHand(hand, word)
            number_of_remaining_letters = calculateHandlen(hand)
            if number_of_remaining_letters == 0:
                print('Run out of letters. Total score: {} points.'.format(acumulated_points))
                break
        elif word == '.':
            print('Goodbye! Total score: {} points.'.format(acumulated_points))
            break
        else:
            print('Invalid word, please try again.\n')


wordList = loadWords()
#playHand({'h':1, 'i':1, 'c':1, 'z':1, 'm':2, 'a':1}, wordList, 7)
#playHand({'w':1, 's':1, 't':2, 'a':1, 'o':1, 'f':1}, wordList, 7)
#playHand({'n':1, 'e':1, 't':1, 'a':1, 'r':1, 'i':2}, wordList, 7)
playHand({'a': 1, 'b': 1, 'o': 1, 'r': 1}, wordList, 7)