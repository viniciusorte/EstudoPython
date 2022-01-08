#Leia o comprimento do cateto oposto e do cateto adjacentede um triângulo retângulo, calcule e mostre o comprimento da hipotenusa

import math
a=float(input('Quanto mede o cateto oposto?'))
b=float(input('Quando mede o cateto adjacente?'))
h=(a**1/2)+(b**1/2)
print('A hipotenusa mede {:.2f}'.format(h))

