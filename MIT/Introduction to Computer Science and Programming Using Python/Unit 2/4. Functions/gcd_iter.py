def gcdIter(a, b):
    '''
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    gcd = 1
    if a > b:
        for i in range(b, 0, -1):
            if a % i == 0 and b % i == 0:
                gcd = i
                break
    else:
        for i in range(a, 0, -1):
            if a % i == 0 and b % i == 0:
                gcd = i
                break
    return gcd

print(gcdIter(2, 12))
