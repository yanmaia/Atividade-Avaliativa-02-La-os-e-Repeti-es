import sys
num=int(input("Informe numero inteiro e positivo para verificarmos se e triangular: "))
contador=1
numerotri=0
if num<0:
    sys.exit("Informe um numero positivo para da certo o calculo")
while  True:
    numerotri=(contador/2) * (2*1+(contador-1)*1)
    contador+=1
    if numerotri == num:    
        sys.exit("E um numero triangular")
    if numerotri> num:
        sys.exit('não e um numero triangular')  


