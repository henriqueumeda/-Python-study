lista = [2, 5, 9, 4]
lista[2] = 3
lista.append(7)
lista.sort()
print(lista)
lista.sort(reverse=True)
print(lista)
print(f'Essa lista tem {len(lista)} elementos')
lista.insert(2, 0)
print(lista)
lista.pop(1)
print(lista)
lista.insert(2, 2)
print(lista)
lista.remove(2) #remove a primeira ocorrência
print(lista)
