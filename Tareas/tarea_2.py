import re

exprCorreo1= '^[a-z]+@[a-z0-9]+.[a-z]+$'
exprCorreo2= '^[a-z]+@[a-z0-9]+.[a-z]+.[a-z]{,5}$'
exprCorreo3= '^[a-z_]+@[a-z0-9]+.[a-z]+.[a-z]{,5}$'

resul= re.match(exprCorreo1,"patds@cinvestav.mx")
print(resul)

resul2= re.match(exprCorreo2,"patds@cinvestav.com.mx")
print(resul2)

resul3 = re.match(exprCorreo3,"patds@cinvestav.subdominio.mx")
print(resul3)

expresNumeroTel = '^[0-9]{10}$'
expresNumeroTel2 = '^([0-9]{2})[0-9]{8}$'


numResul = re.match(expresNumeroTel,"4322323235")
print(numResul)

numResul2 = re.match(expresNumeroTel2,"(12)12345678")
print(numResul2)
