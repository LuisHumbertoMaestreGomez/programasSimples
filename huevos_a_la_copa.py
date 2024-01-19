#Escriba un programa que reciba como entrada la temperatura original del huevo y muestre como salida el tiempo en segundos que le toma alcanzar la temperatura máxima para prepararlo a la copa.

import math
th = float(input("temperaura original del huevo\n"))
te = 100
m = 47
p = 1.038
c = 3.7
k = 0.0054

dividendo = math.pow(m, (2/3)) * (c * (math.pow(p, (1/3))))
divisor = (k * math.pow(math.pi, 2)) * math.pow((4*math.pi) / 3, (2/3))
resultado = dividendo * divisor
resultado2 = math.log(0.76 * ((th - te) / (70 - te)))
segundos = resultado * resultado2
minutos = round(segundos/60)

print(f"el tiempo maximo para prepararlo a la copa {round(segundos)} segundos")
print(f"el tiempo maximo para prepararlo a la copa {minutos} min")
