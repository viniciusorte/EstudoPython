#Preço antigo   % * peso/100
gar=(5.50)
dan=(4.90)
pao=(0.30)
bif=(50.0)

#Valor dos 5% referente ao produto
dg=(5*gar/100)
dd=(5*dan/100)
dp=(5*pao/100)
db=(5*bif/100)

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