def oddTuples(aTup):
    '''
    aTup: a tuple

    returns: tuple, every other element of aTup.
    '''
    odd_tuple = ()
    for number, element in enumerate(aTup):
        if number % 2 == 0:
            odd_tuple += (element, )
    return odd_tuple

aTup = ('I', 'am', 'a', 'test', 'tuple')
print(oddTuples(aTup))
