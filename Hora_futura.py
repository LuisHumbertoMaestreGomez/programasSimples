#Escriba un programa que pregunte al usuario la hora actual t del reloj y un número entero de horas h, que indique qué hora marcará el reloj dentro de h horas:
num = int(input("ingrece la hora actual"))
num2 =int(input("ingrese la cantidad de horas que quiere avanzar"))
suma = num + num2
while suma > 24:
    suma -= 24
if suma > 12:
    suma -= 12
    print(f"en {num2} horas, el relog marcara las {suma} pm")
else:
    print(f"en {num2} horas, el relog marcara las {suma} am")