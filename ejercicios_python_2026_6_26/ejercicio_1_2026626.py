print('Bienvenido a la calculadora de propinas')
elMonto = float(input("ingrese el monto de la comida: "))
elPorcentaje = float(input("ingrese el porcentaje de la propina: "))
cantidadComensales = int(input("ingrese la cantidad de comensales: "))

propina = elMonto * elPorcentaje / 100
total = elMonto + propina
elresultado = total / cantidadComensales

print("El monto que cada uno tiene que pagar es:", round(elresultado, 2))
