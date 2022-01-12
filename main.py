#Leia um ângulo qualquer e mostre na tela o valor de Seno,Cosseno e Tangente desse ângulo

import math
a=float(input('Quanto mede o cateto oposto?'))
b=float(input('Quando mede o cateto adjacente?'))
r=(a**2)+(b**2)
h=r**(1/2)
print('A hipotenusa mede {:.2f}'.format(h))

