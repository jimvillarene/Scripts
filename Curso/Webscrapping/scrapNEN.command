#! /usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time, os
import pandas as pd

# Ruta al controlador del navegador (chromedriver o geckodriver)
#driver_path = 'ruta/al/controlador'

# Crea una instancia del navegador (en este ejemplo, se utiliza Chrome)
driver = webdriver.Chrome()
driver.maximize_window() # For maximizing window
driver.implicitly_wait(20) # gives an implicit wait for 20 seconds

# Abre la página de inicio
driver.get("https://web.nen.wfglobal.org")

# Espera un tiempo para asegurarte de que la página se cargue completamente
time.sleep(3)

# Interactúa con la página de bienvenida (por ejemplo, haz clic en un botón si es necesario)
# Aquí puedes agregar acciones específicas según la estructura de la página

# Luego, navega a la página de inicio de sesión
Wlcmbutton=driver.find_element(By.CSS_SELECTOR,"#app > div > div > div > div > div.container.guest-view-container > div > div > div.ant-col.guest-details-container.ant-col-xs-24.ant-col-lg-12 > div > button")
Wlcmbutton.click()


# Espera un tiempo para asegurarte de que la página se cargue completamente
time.sleep(3)

# Ingresa tus credenciales en los campos correspondientes
boxUser=driver.find_element(By.CSS_SELECTOR,"#app > div > div > div > div > div > div.ant-col.reg_form__right_container.undefined.ant-col-xs-24.ant-col-md-11 > div > div > form > div > div.wf_animated_input.sign_in__input_first")
boxUser.click()
usuario = driver.find_element(By.NAME,"email")
usuario.send_keys("alberto.jimenez@wfglobal.org")
time.sleep(1)

boxPswrd=driver.find_element(By.CSS_SELECTOR,"#app > div > div > div > div > div > div.ant-col.reg_form__right_container.undefined.ant-col-xs-24.ant-col-md-11 > div > div > form > div > div.wf_animated_input.sign_in__input")
boxPswrd.click()

contraseña = driver.find_element(By.NAME,"password")
contraseña.send_keys("Alberto09")
time.sleep(1)


# Envía el formulario
contraseña.send_keys(Keys.RETURN)

# Espera a que la página cargue después del inicio de sesión (ajusta el tiempo según sea necesario)
time.sleep(3)

# Ahora puedes interactuar con la página protegida después del inicio de sesión
# Por ejemplo, puedes extraer información o realizar otras acciones

#Creamos dos elementos, uno para almacenar los elementos web de cohorts y otro para almacenar los detalles de cada cohort
cohorts=[]
cohortDetails = []

#Crear una lista con los elementos de paginación
pages=driver.find_elements(By.CLASS_NAME,"ant-pagination-item")
#obtener el boton de siguiente página
nextBtn=driver.find_element(By.CSS_SELECTOR,"#batch-table > div > div > div > ul > li.ant-pagination-next > button")

for page in range(len(pages)):
    #Tomamos los elementos de la tabla de Cohorts
    cohorts=driver.find_elements(By.CLASS_NAME,"ant-table-row-level-0")
    # Creamos un bucle para vaciar la información de cada columna de cohorts en elementos web
    for children in cohorts:
        childElement = children.find_elements(By.XPATH,'*')
        cohortDetail = {
            'name': '',
            'institute': '',
            'course': '',
            'startDate': '',
            'endDate': '',
            'students': ''
        }
        
        for idx, child in enumerate(childElement):
            text = child.text
            
            if idx == 0:
                cohortDetail['name'] = text
            elif idx == 1:
                cohortDetail['institute'] = text
            elif idx == 2:
                cohortDetail['course'] = text
            elif idx == 3:
                cohortDetail['startDate'] = text
            elif idx == 4:
                cohortDetail['endDate'] = text
            elif idx == 5:
                cohortDetail['students'] = text
        
        cohortDetails.append(cohortDetail)

    # Ir a la siguiente página
    if page < len(pages)-1 and nextBtn.is_enabled():
        nextBtn.click()
        time.sleep(5)  # Asegurarse de que la página se cargue completamente

# Crear un dataframe a partir de la lista de diccionarios
df = pd.DataFrame(cohortDetails)

# Guardar el dataframe en un archivo Excel
dir_path = os.path.dirname(os.path.realpath(__file__))
excel_filename = os.path.join(dir_path,"cohort_details.xlsx")

df.to_excel(excel_filename, index=False)

# Abrir el archivo Excel
path_to_excel="'/Applications/Microsoft Excel.app'"
os.system("open "+path_to_excel+" " + excel_filename)

# Cierra el navegador
driver.quit()

'''
# Import libraries
import requests
from bs4 import BeautifulSoup
 
# URL from which pdfs to be downloaded
url = "https://www.geeksforgeeks.org/how-to-extract-pdf-tables-in-python/"
 
# Requests URL and get response object
response = requests.get(url)
 
# Parse text obtained
soup = BeautifulSoup(response.text, 'html.parser')
 
# Find all hyperlinks present on webpage
links = soup.find_all('a')
 
i = 0
 
# From all links check for pdf link and
# if present download file
for link in links:
    if ('.pdf' in link.get('href', [])):
        i += 1
        print("Downloading file: ", i)
 
        # Get response object for link
        response = requests.get(link.get('href'))
 
        # Write content in pdf file
        pdf = open("pdf"+str(i)+".pdf", 'wb')
        pdf.write(response.content)
        pdf.close()
        print("File ", i, " downloaded")
 
print("All PDF files downloaded")
'''