#! /usr/bin/env python3
# Import libraries
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time, os, re
import pandas as pd

def loginNEN(user,password):
    # Luego, navega a la página de inicio de sesión
    Wlcmbutton=driver.find_element(By.CSS_SELECTOR,"#app > div > div > div > div > div.container.guest-view-container > div > div > div.ant-col.guest-details-container.ant-col-xs-24.ant-col-lg-12 > div > button")
    Wlcmbutton.click()


    # Espera un tiempo para asegurarte de que la página se cargue completamente
    time.sleep(3)

    # Ingresa tus credenciales en los campos correspondientes
    boxUser=driver.find_element(By.CSS_SELECTOR,"#app > div > div > div > div > div > div.ant-col.reg_form__right_container.undefined.ant-col-xs-24.ant-col-md-11 > div > div > form > div > div.wf_animated_input.sign_in__input_first")
    boxUser.click()
    usuario = driver.find_element(By.NAME,"email")
    usuario.send_keys(user)
    time.sleep(1)

    boxPswrd=driver.find_element(By.CSS_SELECTOR,"#app > div > div > div > div > div > div.ant-col.reg_form__right_container.undefined.ant-col-xs-24.ant-col-md-11 > div > div > form > div > div.wf_animated_input.sign_in__input")
    boxPswrd.click()

    contraseña = driver.find_element(By.NAME,"password")
    contraseña.send_keys(password)
    time.sleep(1)


    # Envía el formulario
    contraseña.send_keys(Keys.RETURN)

    # Espera a que la página cargue después del inicio de sesión (ajusta el tiempo según sea necesario)
    time.sleep(3)


def scrap_cohorts():
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

    # Preguntamos si quiere guardar en excel la información
    export_Excel = input("¿Quiéres guardar una copia de la información de los cohorts en Excel? \n y/n : ")

    if export_Excel =='y' or export_Excel== 'yes':
        # Guardar el dataframe en un archivo Excel
        dir_path = os.path.dirname(os.path.realpath(__file__))
        excel_filename = os.path.join(dir_path,"cohort_details.xlsx")

        df.to_excel(excel_filename, index=False)

        # Abrir el archivo Excel
        path_to_excel="'/Applications/Microsoft Excel.app'"
        os.system("open "+path_to_excel+" " + excel_filename)

    # Crear una nueva lista únicamente con los nombres de los cohorts
    selected_columns = df[['name']].copy()

    # Mostrar la nueva lista con las primera columna en batches de 10
    batch_size = 10
    num_batches = len(selected_columns) // batch_size + 1
    current_batch = 1
    while current_batch <= num_batches:
        start_idx = (current_batch - 1) * batch_size
        end_idx = min(current_batch * batch_size, len(selected_columns))
        batch_data = selected_columns[start_idx:end_idx]
        
        # Mostrar el batch actual
        print(f"Lote de cohorts {current_batch} de {num_batches}:")
        print(batch_data)
        
        if current_batch < num_batches:
            input("Presiona enter para continuar...")
        
        current_batch += 1

    # Elegir una fila para ver a detalle
    selected_row = int(input("Ingresa el número de la fila que deseas ver a detalle: ")) 

    if 0 <= selected_row < len(selected_columns):
        name_selected = selected_columns.iloc[selected_row]['name']
        print(f"Detalles para la fila seleccionada ({name_selected}):")
        print(df[df['name'] == name_selected])
    else:
        print("Número de fila no válido.")
    
    return selected_row



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

loginNEN("alberto.jimenez@wfglobal.org","Alberto09")

# Ahora puedes interactuar con la página protegida después del inicio de sesión
# Por ejemplo, puedes extraer información o realizar otras acciones
selected_cohort=scrap_cohorts()
# Buscamos en qué página está el cohort y qué número de cohort en la página es
page=selected_cohort//10
mod10=selected_cohort%10
print(page,mod10)
# Hacemos un array con todos los botones de página
pageButtons=driver.find_elements(By.CLASS_NAME,"ant-pagination-item")
pageBtn=pageButtons[page]
pageBtn.click()

#Creamos dos elementos, uno para almacenar los elementos web de cohorts y otro para almacenar los detalles de cada cohort
cohorts=[]
cohorts=driver.find_elements(By.CLASS_NAME,"ant-table-row-level-0")
cohort=cohorts[mod10]
cohort.click()
time.sleep(10)


# Cierra el navegador
driver.quit()
