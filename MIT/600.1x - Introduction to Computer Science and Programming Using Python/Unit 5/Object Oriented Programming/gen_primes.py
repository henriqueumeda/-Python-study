def genPrimes():
    primes = [2]
    x = 2
    while True:
        for prime_number in primes:
            if (x % prime_number) == 0 and x != 2:
                x += 1
                break
            elif prime_number == primes[-1]:
                if x not in primes:
                    primes.append(x)
                yield x
                x += 1
                break
