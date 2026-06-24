import re

def limpiar_saltos_de_linea(texto):
    # 1. Unir palabras cortadas con guión
    texto = re.sub(r'-\n', '', texto)
    # 2. Reemplazar saltos de línea por espacios
    texto = re.sub(r'\n', ' ', texto)
    # 3. Quitar espacios dobles que puedan quedar
    texto = re.sub(r' +', ' ', texto)
    return texto.strip()