contador = soma = 0

while True:
    numero = int(input('Digite um valor inteiro (999 para parar): '))
    if numero == 999:
        break
    soma += numero
    contador += 1

print(f'A soma dos {contador} valores foi {soma}')