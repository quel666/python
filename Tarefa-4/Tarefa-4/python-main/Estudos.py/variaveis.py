faturamento = 1200 # número inteiro (int)
custo = 770 

novas_vendas = 300 # Eu posso usar "_" para juntar palavras na variável

taxa_imposto = 0.5 # Para colocar porcentagem é necessário ser em decimal (float) e não esquecer do ponto

imposto = taxa_imposto * faturamento

print ("Faturamento:", faturamento)
print ("Custo:", custo)
print ("Lucro:", faturamento - custo - imposto)
