##curso basico de python
#nome do desevolvedor: Raquel Ferreira Rocha
#versão 1.0
#exercicio de logica de programação 
#com a linguagem de programação python
#exercicio do lado do hexagono

import math

lado = int(input ("digite o valor do lado de um hexagono "))

resultado = ((3*pow(lado,2)*math.sqrt(3))/2)
#math sqrt: raiz quadrada 
#pow : exponenciação 

print ("A area do hexagono é ", round(resultado), "m²")
#Round: arredondamento do numero do resultado

