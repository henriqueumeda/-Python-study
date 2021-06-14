def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])

def absolute(a):
    return abs(a)

testList = [1, -4, 8, -9]

applyToEach(testList, absolute)

print(testList)
