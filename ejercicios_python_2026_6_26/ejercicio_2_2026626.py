print('bien venido a la calculadora de propinas\n')
elMonto=float(input("ingrese el monto de la comida\n"))
elPorcentaje=float(input("ingrese el porcentaje de la propina\n"))
cantidadComensales=int(input("ingrese la cantidad de comensales\n"))
elresultado = ((elMonto * elPorcentaje) / 100) / cantidadComensales
print("El monto de la propina que cada uno tiene que pagar es: \n")
print(elresultado)

# https://www.mycompiler.io/es/new/python
