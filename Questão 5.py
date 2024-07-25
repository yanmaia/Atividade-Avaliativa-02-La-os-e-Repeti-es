import sys
num=int(input('Informe um numero inteiro positivo para contarmos o tamanho: '))
contador=0
if num <0:
    sys.exit('Informe um numero positivo')
else:
    while num > 0:
        num//= 10
        contador+=1
print(f'o Valor informado possui {contador} Digitos')