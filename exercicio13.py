numero = int (input("Digite um número: "))

if numero <= 1:
    print ("O numero não é primo: ")

elif numero%2==0 and numero!=2:
    print ("O número não é primo: ")

elif numero%3==0 and numero!=3 or numero%5==0 and numero!=5 or numero%7==0 and numero!=7:
    print ("O número não é primo")

else:
    print ("O numero é primo")