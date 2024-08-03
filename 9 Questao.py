import sys
num=int(input("Informe um numero inteiro positivo:"))
contadortam=0
nums=str(num)
soma=0
if num <0:          
    sys.exit('Informe um numero positivo para ser valido')
else:
    while num > 0:           #Descobre o tamanho do numero informado
        num//= 10
        contadortam+=1
    for i in nums:
        soma+=  int(i)** contadortam     #Faz o calculo de potenciação para checagem do armstrong
if int(nums) == soma:                              #checagem do numero
    print('E um número Armstrong')
else: 
    print('Não e um número Armstrong') 