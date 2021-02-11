test = list()
test.append('Gustavo')
test.append(40)
guys = list()
guys.append(test[:])
test[0] = 'Maria'
test[1] = 22
guys.append(test[:])
print(guys)
