wordList = ['quail']
def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.

    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    if len(word) == 0:
        return False

    for letter in word:
        if word.count(letter) > hand.get(letter, 0) or word not in wordList:
            return False
    return True

hand = {'a':1, 'q':1, 'l':2, 'm':1, 'u':1, 'i':1}
print(isValidWord('quail', hand, wordList))