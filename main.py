salario=float(input('Qual salário do funcionário? R$'))

#Valor dos 5% referente ao produto
desconto=(15*salario/100)

#Preço já com desconto
sd=salario+desconto
                                      
print('Seu salário de R${}, aumentou para R${} pois aplicamos um aumento de 15% o que equivale a R${} a mais'.format(salario,sd,desconto))
