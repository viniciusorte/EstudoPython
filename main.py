# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
km=float(input('Quanto Km rodados?'))
dia=int(input('Quantos dias alugados?'))
preço=(dia*60)+(km*0.15)
print('Voce tem que pagar {:.2f} pois você alugou o carro por {} dias e andou {}km com ele'.format(preço,dia,km))