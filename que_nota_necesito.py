#Escriba un programa que pregunte al usuario las notas de los dos primeros certamen y la nota de laboratorio, y muestre la nota que necesita el alumno para aprobar el ramo con nota final 60.
c1 = int(input("ingrece la primera nota del certamen"))
c2 = int(input("ingrece la segunda nota del certamen"))
nl = int(input("ingrece una nota de laboratorio"))

nc = (59.5 - 0.3 * nl)/0.7
c3 = 3 * nc - (c1 + c2) + 1

print("necesita nota", int(round(c3)), "en el certamen 3")