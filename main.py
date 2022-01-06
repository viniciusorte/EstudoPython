#Preço antigo   % * peso/100
gar=float(5.50)
dan=float(4.90)
pao=float(0.30)
bif=float(50.0)

#Valor dos 5% referente ao produto
dg=float(5*gar/100)
dd=float(5*dan/100)
dp=float(5*pao/100)
db=float(5*bif/100)

#Preço já com desconto
pg=gar-dg
pd=dan-dd
pp=pao-dp
pb=bif-db                                       

print('Siga a lista de descontos:') 
print('Garrafa estava custando {:.2f}, com 5% de desconto agora está custando R${:.2f} '.format(gar,pg))
print('Danoninho estava custando {:.2f}, com 5% de desconto agora está custando{:.2f}'.format(dan,pd))
print('Pãozinho estava custando {:.2f}, com 5% de desconto agora está custando R${:.2f}'.format(pao,pp))
print('Bifão estava custando {:.2f}, com 5% de desconto agora está custando R${:.2f}'.format(bif,pb))
