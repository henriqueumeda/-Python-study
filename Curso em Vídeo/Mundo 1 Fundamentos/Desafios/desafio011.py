largura = float(input('Digite a largura da parede (em metros): '))
altura = float(input('Digite a altura da parede (em metros): '))
area = largura * altura
tinta = area / 2
print('A parede tem {}m² e serão necessários {} litros de tinta para pintá-la.'.format(area, tinta))