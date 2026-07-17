gastos={
    "comida":{"desayuno":0,"almuerzo":2,"merienda":3},
    "transporte":{"al trabajo":0,"a casa":0}
}
verdad = True

def ingresa_tu_gasto():
    global gastos
    laCategoria = input("ingresa la categoria\n")
    elNombre = input("ingresa el nombre\n")
    elGasto = input("ingresa el monto\n")
    try:
        gastos[laCategoria][elNombre]+=int(elGasto)
    except KeyError:
        print("Categoría o nombre no válido")
    except ValueError:
        print("El monto debe ser un número")

# print(gastos)

def sumar_gastos():
    contar_02 = 0
    global gastos
    for categoria in gastos.values():
        for nombre in categoria.values():
            contar_02+=nombre
    print(f"la sumatoria es:  {contar_02}")

while verdad:
    try:
        desea_salir = int(input("""ingrese 0 si desea salir\n
        ingrese 1 si desea ingresar su gasto\n
        ingrese 2 si desea la sumatoria del gasto\n"""))
        if desea_salir ==0:
                verdad = False
        elif desea_salir == 1:
            ingresa_tu_gasto() 
        elif desea_salir == 2:
            sumar_gastos() 
    except ValueError:
        print("Por favor, ingrese un número válido")

