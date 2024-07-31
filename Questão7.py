import sys
vinicial=int(input('Informe um valor inteiro inicial da PA: '))
razaopa=float(input('Informe a Razao da PA: '))
vquantidade=int(input('Informe a quantidade de elementos positivo de uma  PA: '))
valorpa=vinicial
#valorpa2=valorpa
soma=vinicial
#lista=' '
if vquantidade<0:           #Verifica se e positivo 
    sys.exit('Informe quantidade de elementos positivos da PG')
elif razaopa == 0:
    print('A PA e  uma constante')
elif razaopa>0:    
    print('A PA e uma crescente')
elif razaopa<0:
    print('A PA e  uma decrescente')
print(f'o valor da PA({1})= {valorpa:,} ')
for i in range (2,vquantidade+1):     
    print(f'o valor da PA({i})={valorpa:,} + {razaopa} = {valorpa+razaopa}')
    valorpa=vinicial+(i-1)*razaopa
    soma+=valorpa
    #lista+= str(valorpa2)
    

print(f'A soma dos valores dessa PA são: {soma:,} ')

#num=int(input('informe um outro valor inteiro que corresponde  a enezima posição dessa PG: '))
 #   sys.exit('Informe uma quantidade de elementos positivos da PG')           
#termoene= vinicial *(razaopg**(num-1))      #Calcula o valor de uma PG em uma enezima posição
#print(f'o valor da enezima posição  {num} e {termoene:,}')
