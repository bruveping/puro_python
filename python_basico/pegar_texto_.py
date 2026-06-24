import re
elTexto = """
Nadie puede concebir la variedad de sentimientos que, en el primer entu-
siasmo por el éxito, me espoleaban como un huracán. La vida y la muerte
me parecían fronteras imaginarias que yo rompería el primero, con el fin
de desparramar después un torrente de luz por nuestro tenebroso mundo.
Una nueva especie me bendeciría como a su creador, muchos seres felices y
maravillosos me deberían su existencia. Ningún padre podía reclamar tan
completamente la gratitud de sus hijos como yo merecería la de éstos. Pro-
siguiendo estas reflexiones, pensé que, si podía infundir vida a la materia
inerte, quizá, con el tiempo (aunque ahora lo creyera imposible), pudiese
devolver la vida a aquellos cuerpos que, aparentemente, la muerte había
entregado a la corrupción.
"""

ElPatron = "-\n"

textoProcesado = re.sub(ElPatron,"",elTexto)

print(textoProcesado)
nuevoPatron="\n"
textoSinSalto = re.sub(nuevoPatron," ",textoProcesado)
print(textoSinSalto)