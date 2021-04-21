from math import sqrt

def stdDevOfLengths(L):
    """
    L: a list of strings

    returns: float, the standard deviation of the lengths of the strings,
      or NaN if L is empty.
    """
    number_of_strings = len(L)
    if number_of_strings == 0:
        return float('NaN')
    numerator = 0
    string_length_sum = 0
    for element in L:
        string_length_sum += len(element)
    average_length = string_length_sum/number_of_strings
    for element in L:
        numerator += (len(element) - average_length)**2
    standard_deviation = sqrt(numerator/number_of_strings)
    return standard_deviation

L = ['a', 'z', 'p']
L = ['apples', 'oranges', 'kiwis', 'pineapples']
print(stdDevOfLengths(L))
