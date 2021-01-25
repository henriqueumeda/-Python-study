print('-=' * 13)
print('Analisador de Triângulos')
print('-=' * 13)

primeiroSegmento = float(input('Primeiro segmento: '))
segundoSegmento = float(input('Segundo segmento: '))
terceiroSegmento = float(input('Terceiro segmento: '))

lados = [primeiroSegmento, segundoSegmento, terceiroSegmento]
lados.sort()

if lados[2] < lados[0] + lados[1]:
    print('Os segmentos acima PODEM FORMAR um triângulo!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR um triângulo!')
