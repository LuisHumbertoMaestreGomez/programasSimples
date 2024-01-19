#Escriba un programa que reciba como entrada las longitudes de los dos catetos a
#y b de un triángulo rectángulo, y que entregue como salida el largo de la hipotenusa c
#del triangulo, dado por el teorema de Pitágoras:
lado  = float(input("ingrece el primer lado del triangulo\n"))
lado2 = float(input("ingrece el segundo lado del triangulo\n"))
hipótenusa = (lado**2 + lado2**2)**0.5
print(f"la hipotenusa es {hipótenusa}")