from math import sqrt

def stdDevOfNumbers(L):
    """
    L: a list of strings

    returns: float, the standard deviation of the lengths of the strings,
      or NaN if L is empty.
    """
    number_of_elements = len(L)
    if number_of_elements == 0:
        return float('NaN')
    numerator = 0
    number_sum = 0
    for element in L:
        number_sum += element
    average = number_sum/number_of_elements
    for element in L:
        numerator += (element - average)**2
    standard_deviation = sqrt(numerator/number_of_elements)
    return standard_deviation

L = [10, 4, 12, 15, 20, 5]
number_sum = 0
for element in L:
    number_sum += element
mean = number_sum/len(L)
print(stdDevOfNumbers(L)/mean)
