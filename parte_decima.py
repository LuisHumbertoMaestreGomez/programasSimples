#Escriba un programa que entregue la parte decimal de un número real ingresado por el usuario.
numero = float(input("ingrese un numero real"))
decimal = round(numero - int(numero), 2)
print(f"la parte decimal de {numero} es:\n {decimal}")
