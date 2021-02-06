primeiro_segmento = float(input('Primeiro segmento: '))
segundo_segmento = float(input('Segundo segmento: '))
terceiro_segmento = float(input('Terceiro segmento: '))
lados = [primeiro_segmento, segundo_segmento, terceiro_segmento]
lados.sort()

if lados[2] >= lados[0] + lados[1]:
    print('Os segmentos acima NÃO PODEM FORMAR um triângulo')
elif lados[2] == lados[1] == lados[0]:
    print('Os segmentos acima PODEM FORMAR um triângulo EQUILÁTERO!')
elif lados[2] != lados[1] != lados[0]:
    print('Os segmentos acima PODEM FORMAR um triângulo ESCALENO!')
else:
    print('Os segmentos acima PODEM FORMAR um triângulo ISÓSCELES!')
