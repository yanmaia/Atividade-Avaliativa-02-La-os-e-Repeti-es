import sys
vinicial=int(input('Informe um valor inteiro inicial da PA: '))
razaopa=float(input('Informe a Razao da PA: '))
vquantidade=int(input('Informe a quantidade de elementos positivo de uma  PA: '))
valorpa=vinicial
valorpa2=valorpa
soma=0
lista=' '
#if vquantidade<0:           #Verifica se e positivo 
   # sys.exit('Informe quantidade de elementos positivos da PG')
#elif razaopg == 1:
  #  print('A PG e  uma constante')
#elif razaopg < 0 :
 #   print('A PG e uma Oscilante')
#elif valorpg >= 1 < razaopg or 0<razaopg<1>valorpg<0:
#    print('A PG e uma crescente')
#elif 0<razaopg<1:
#    print('A PG e  uma decrescente')

for i in range (1,vquantidade+1):     
    valorpa2=valorpa+(i-1)*razaopa
    lista+= str(valorpa2)
    print(f'o valor da PA({i})= {valorpa2:,} ')
#print(f'Os termos da PA são {lista}')
#print(f'A soma dos valores dessa PA são: {valorpa:,}')

#num=int(input('informe um outro valor inteiro que corresponde  a enezima posição dessa PG: '))
#if num < 0:                       #Verifica se e positivo
 #   sys.exit('Informe uma quantidade de elementos positivos da PG')           
#termoene= vinicial *(razaopg**(num-1))      #Calcula o valor de uma PG em uma enezima posição
#print(f'o valor da enezima posição  {num} e {termoene:,}')