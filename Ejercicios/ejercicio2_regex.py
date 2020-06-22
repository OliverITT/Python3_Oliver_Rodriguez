import re

noletras = '[^a-zA-Z]+$'

result = re.match(noletras,"123#.")
print(result)

soloNum = '[0-9]+$'
result = re.match(soloNum,"123")
print(result)

soloLetraMayus = '[A-Z]+$'
result = re.match(soloLetraMayus,"AA")
print(result)

soloMinusculas = '[a-z]+$'
result = re.match(soloMinusculas,"aasdgba")
print(result)

noNumeros='[^0-9]+$'
result = re.match(noNumeros,"adg··##AAg'")
print(result)