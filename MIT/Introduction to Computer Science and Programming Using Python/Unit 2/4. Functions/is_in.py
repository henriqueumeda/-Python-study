def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string

    returns: True if char is in aStr; False otherwise
    '''
    if len(aStr) <= 1:
        return False

    middle_position = int(len(aStr)/2)
    middle_char = aStr[middle_position]
    if char == middle_char:
        return True
    elif char != middle_char and middle_position == 0:
        return False
    else:
        if char > middle_char:
            aStr = aStr[middle_position:]
        else:
            aStr = aStr[:middle_position]
        return isIn(char, aStr)

print(isIn('c', 'abdefghijklmn'))
