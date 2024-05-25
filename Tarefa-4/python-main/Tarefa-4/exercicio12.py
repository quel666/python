nota1 = int (input("Digite sua nota da primeira avaliação: "))
nota2 = int (input("Digite sua nota da segunda avaliação: "))
media = (nota1+nota2)/2

if media > 6:
    print ("Você foi aprovado", media)

else:
    print ("Você não foi aprovado", media)
