total_de_eleitores = int (input("Digite o total de eleitores do município:"))
numero_de_votos_brancos = int (input("Digite o número de votos brancos:"))
votos_nulos = int (input("Digite o número de votos nulos:"))
votos_validos = int (input("Digite o número de votos validos:"))

percentual = (total_de_eleitores / numero_de_votos_brancos / votos_nulos / votos_nulos) /100

print ("O percentual é: ", percentual)