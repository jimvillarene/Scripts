import re
import pandas as pd

# Texto completo
texto_completo = """

"""

# Expresiones regulares para identificar los límites de cada sección (insensibilidad a mayúsculas/minúsculas)
expresion_1 = r"(.*?)¿CUÁL ES TU TIPO DE MERCADO\?"
expresion_2 = r"(.*?)Cuadro comparativo de la competencia"
expresion_3 = r"(.*?)Marketing y Ventas"

# Encontrar las secciones utilizando expresiones regulares
seccion_1 = re.search(expresion_1, texto_completo, re.DOTALL | re.IGNORECASE).group(1)
seccion_2 = re.search(expresion_2, texto_completo, re.DOTALL | re.IGNORECASE).group(1)
seccion_3 = re.search(expresion_3, texto_completo, re.DOTALL | re.IGNORECASE).group(1)
seccion_4 = re.sub(expresion_3, "", texto_completo, 1, re.DOTALL | re.IGNORECASE)

# Crear un diccionario con las secciones
diccionario_secciones = {
    'Milestone 1': seccion_1.strip(),
    'Milestone 2': seccion_2.strip(),
    'Milestone 3': seccion_3.strip(),
    'Milestone 4': seccion_4.strip()
}

# Crear un DataFrame a partir del diccionario
df = pd.DataFrame.from_dict(diccionario_secciones, orient='index', columns=['Contenido'])

# Guardar el DataFrame en un archivo Excel
excel_filename = "secciones.xlsx"
df.to_excel(excel_filename)

print("Secciones guardadas en el archivo Excel:", excel_filename)