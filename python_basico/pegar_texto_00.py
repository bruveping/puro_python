import re

def pegaTexto(cambia_texto):
    elPatron = "-\n"
    Proceso1texto = re.sub(elPatron, "", cambia_texto)
    elPatron2 ="\n"
    Proceso2texto = re.sub(elPatron2, " ", Proceso1texto)
    return Proceso2texto



cambia_texto = """
Estos pensamientos me animaban, mientras proseguía mi trabajo con infa-
tigable entusiasmo. El estudio había empalidecido mi rostro, y el constante
encierro me había demacrado. A veces fracasaba al borde mismo del éxito,
pero seguía aferrado a la esperanza que podía convertirse en realidad al
día o a la hora siguiente. El secreto del cual yo era el único poseedor era
la ilusión a la que había consagrado mi vida. La luna iluminaba mis esfuer-
zos nocturnos mientras yo, con infatigable y apasionado ardor, perseguía
a la naturaleza hasta sus más íntimos arcanos. ¿Quién puede concebir los
horrores de mi encubierta tarea, hurgando en la húmeda oscuridad de las
tumbas o atormentando a algún animal vivo para intentar animar el barro
inerte?
"""

print(pegaTexto(cambia_texto))
