import math
angulo = float(input('Digite o ângulo que você deseja (somente números, em graus): '))
anguloRad = math.radians(angulo)
seno = math.sin(anguloRad)
cosseno = math.cos(anguloRad)
tangente = math.tan(anguloRad)
print('O ângulo de {:.1f}º tem o SENO de {:.2f}'.format(angulo, seno))
print('O ângulo de {:.1f}º tem o COSSENO de {:.2f}'.format(angulo, cosseno))
print('O ângulo de {:.1f}º tem a TANGENTE  de {:.2f}'.format(angulo, tangente))