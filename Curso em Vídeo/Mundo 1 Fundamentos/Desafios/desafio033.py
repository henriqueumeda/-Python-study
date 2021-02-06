primeiroValor = float(input('Primeiro valor: '))
segundoValor = float(input('Segundo valor: '))
terceiroValor = float(input('Terceiro valor: '))
lista = [primeiroValor, segundoValor, terceiroValor]
print('O \033[35mmenor\033[m valor digitado foi \033[35m{}\033[m'.format(min(lista)))
print('O \033[33mmaior\033[m valor digitado foi \033[33m{}'.format(max(lista)))
