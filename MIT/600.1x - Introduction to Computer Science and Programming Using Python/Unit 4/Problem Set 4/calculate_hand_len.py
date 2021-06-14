def calculateHandlen(hand):
    """
    Returns the length (number of letters) in the current hand.

    hand: dictionary (string int)
    returns: integer
    """
    hand_len = 0
    for frequency in hand.values():
        hand_len += frequency
    return hand_len

hand = {'a':1, 'q':1, 'l':2, 'm':1, 'u':1, 'i':1}
print(calculateHandlen(hand))
