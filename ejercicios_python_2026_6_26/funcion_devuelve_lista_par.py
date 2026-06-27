def solo_pares(elInput):
  laLista = []
  numeros_palabra = []
  listaDefinitiva =[]

  print(f" el nuero ingresado es: {elInput}")

  for esto in elInput.split():
      numeros_palabra.append(esto)


  for esto in numeros_palabra:
      laLista.append(int(esto))

  # print(numeros_palabra)
  # print(laLista)

  for par in laLista:
      if (par % 2 == 0):
        listaDefinitiva.append(par)
  return listaDefinitiva


laFuncion = solo_pares(input("\n ingresa un número mayor que 0\n"))

print(f" el resultado es: {laFuncion}")
