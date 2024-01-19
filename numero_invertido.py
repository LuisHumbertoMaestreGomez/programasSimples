#Escriba un programa que pida al usuario un entero de tres dígitos, y entregue el número con los dígitos en orden inverso:
nombre = input("ingrese un numero:")
array = []
for i in range(len(nombre)):
    array.append(nombre[-i-1])
print("".join(array))