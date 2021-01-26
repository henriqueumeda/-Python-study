print('\033[33m-=' * 13)
print('Analisador de Triângulos')
print('-=' * 13 + '\033[m')

primeiroSegmento = float(input('Primeiro segmento: '))
segundoSegmento = float(input('Segundo segmento: '))
terceiroSegmento = float(input('Terceiro segmento: '))

lados = [primeiroSegmento, segundoSegmento, terceiroSegmento]
lados.sort()

if lados[2] < lados[0] + lados[1]:
    print('Os segmentos acima \033[1;34mPODEM FORMAR\033[m um triângulo!')
else:
    print('Os segmentos acima \033[1;31mNÃO PODEM FORMAR\033[m um triângulo!')
