import sys
n1=int(input('Informe algum numero inteiro positivo: '))
n2=int(input('Informe algum numero inteiro positivo: '))
dividendo=n1
divisor=n2
resto= n1%n2
if (n1 or n2) <= 0:
    sys.exit('informe um numero inteiro e positivo')
elif n1 == n2:
    sys.exit(f'O mdc e {n1}')
    
while resto != 0:
    dividendo=divisor
    divisor=resto
    resto= dividendo%divisor
print(divisor)