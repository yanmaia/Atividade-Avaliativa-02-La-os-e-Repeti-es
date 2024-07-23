ma=float(input('Informe quantas gramas tem o material radioativo:'))
s=0
mf= ma 
while mf>0.5:
    mf/=2
    s+= 50
h= s // 3600      
res= s % 3600
m= res // 60
seg= res % 60
print(f'Massa inicial:{ma:.0f} gramas\nMassa final:{mf} gramas\nTempo de Decaimento: {h}:{m}:{seg}')