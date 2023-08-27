#! /usr/bin/env python3
# Import libraries
#Libraries for downloading PDF
import requests
from bs4 import BeautifulSoup
#Libraries for webscrapping
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
#Misc Libraries
import time, os, logging
import pandas as pd


# Localizar el folder donde está el archivo de Python
dir_path = os.path.dirname(os.path.realpath(__file__))

#Inicialización del Logging, creamos el archivo de logging
debugFile=os.path.join(dir_path,'scrapBPI_logging.txt')
logging.basicConfig(filename=debugFile ,level=logging.DEBUG, format='%(asctime)s-%(levelname)s-%(message)s') #filename gets all the errors into a textfile
logging.disable(logging.DEBUG) #This one disables all logging, so commenting it out cleans all logging messages from critical to lower, othe levels are DEBUG, INFO, WARNING, ERROR, CRITICAL
logging.info(' Start of program '.center(80,"#"))

def login_NEN(login_mail,login_password):
    try:
        logging.info(' Attempting login '.center(80,"#"))
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
        usuario.send_keys(login_mail)
        time.sleep(1)

        boxPswrd=driver.find_element(By.CSS_SELECTOR,"#app > div > div > div > div > div > div.ant-col.reg_form__right_container.undefined.ant-col-xs-24.ant-col-md-11 > div > div > form > div > div.wf_animated_input.sign_in__input")
        boxPswrd.click()

        contraseña = driver.find_element(By.NAME,"password")
        contraseña.send_keys(login_password)
        time.sleep(1)


        # Envía el formulario
        contraseña.send_keys(Keys.RETURN)

        # Espera a que la página cargue después del inicio de sesión (ajusta el tiempo según sea necesario)
        time.sleep(3)
        logging.info(' login successfull :) '.center(80,"#"))
    except Exception as x:
        logging.info(' login unsuccessfull :( Error: %s'.center(80,"-") %x)


#Función para viajar a la página donde se encuentra el cohort
def locate_cohort(selected_cohort):
    try:
        logging.info(' locating cohort '.center(80,"#"))
        page=selected_cohort//10
        mod10=selected_cohort%10
        #print(page,mod10)
        # Hacemos un array con todos los botones de página
        pageButtons=driver.find_elements(By.CLASS_NAME,"ant-pagination-item")
        pageBtn=pageButtons[page]
        pageBtn.click()
        time.sleep(3)

        #Creamos dos elementos, uno para almacenar los elementos web de cohorts y otro para almacenar los detalles de cada cohort
        cohorts=[]
        cohorts=driver.find_elements(By.CLASS_NAME,"ant-table-row-level-0")
        cohort=cohorts[mod10]
        cohort.click()
        logging.info(' cohort located successfully :) '.center(80,"#"))

        time.sleep(3)
    except Exception as x:
        logging.info(' problem during cohort location :( Error: %s'.center(80,"-")%x)


#Función para obtener el listado de los cohorts
def scrap_cohorts():
    try:
        logging.info(' strating cohort scrapping '.center(80,"#"))
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
        logging.info(' cohorts scrapped succesfully :) '.center(80,"#"))
        return selected_row
    
    except Exception as x:
        logging.info(' Error during cohort scrapping :( Error: %s'.center(80,"-")%x)

    finally:
            driver.get('https://web.nen.wfglobal.org/es/home')

#Función para abrir la página de Milestone desde la página principal
def openMilestone(milestone=1):
    try:
        logging.info(' login successfull :) '.center(80,"#"))
        #HAcemos una lista de las pestañas de navegación
        nav_tabs=[]
        nav_tabs=driver.find_elements(By.CLASS_NAME,'ant-tabs-tab-btn')
        # HAcemos click en la segunda pestaña de navegación "Liberar Módulo"
        liberar_milestone=nav_tabs[1]
        liberar_milestone.click()

        time.sleep(3)

        # HAcemos una lista de la tabla de milestones
        milestones_table = driver.find_element(By.CLASS_NAME, 'milestone-listing-table')
        milestone_rows = milestones_table.find_elements(By.TAG_NAME, 'tr')

        # Verificamos si hay al menos una fila de milestone
        if len(milestone_rows) > 0:
            # Obtenemos la primera fila de milestone, brincándonos la fila de encabezados
            primera_fila = milestone_rows[milestone]
            
            # Obtenemos todas las celdas de la primera fila
            celdas = primera_fila.find_elements(By.TAG_NAME, 'td')
            
            # Verificamos si hay al menos cuatro celdas en la fila
            if len(celdas) > 4:
                # Obtenemos la quinta celda (índice 4) de la primera fila y hacemos clic en ella
                cuarta_celda = celdas[4]
                cuarta_celda.click()
                
                # Espera a que la página cargue después de hacer clic en la celda
                time.sleep(3)
            else:
                print("No hay suficientes celdas en la fila de milestones")
        else:
            print("No se encontraron filas de milestones")
        logging.info(' milestone located successfully :) '.center(80,"#"))
        return
    except Exception as x:
        logging.info(' error during milestone location :( Error: %s'.center(80,"-")%x)


#Función para descargar los pdfs en la carpeta contenedora
def download_ventures(driver, dir_path, milestone):
    try:
        logging.info(' Downloading milestone deliveries '.center(80, "#"))
        time.sleep(5)
        #We Webscrap each element to get the pdf
        if driver.find_element(By.CLASS_NAME, 'secondary_button').is_enabled():
                    moreBtn = driver.find_element(By.CLASS_NAME, 'secondary_button')
                    moreBtn.click()
                    time.sleep(1)

        ventures=[]
        deliveries_table = driver.find_element(By.CLASS_NAME, 'milestone-list-container')
        rows = deliveries_table.find_elements(By.CLASS_NAME, 'checkbox_column_container')
        for row in rows:
                venture_name_element = row.find_element(By.CLASS_NAME, 'venture-name')
                ventures.append(venture_name_element)  # Append the text, not the element itself



        for i in range(len(ventures)):
            time.sleep(4)
            venture_name = ventures[i].text
            actual_milestone = "Milestone " + str(milestone)
            pdf_name = venture_name + " " + actual_milestone + ".pdf"
            pdf_file = os.path.join(dir_path, pdf_name)

            if not ventures[i].is_enabled():
                time.sleep(5)
            ventures[i].click()
            time.sleep(7)
            iframes = driver.find_elements(By.TAG_NAME, 'iframe')
            pdf_url = iframes[0].get_attribute('src')
            #print(pdf_url)

            statement_page = download_pdf(pdf_url, venture_name)

            with open(pdf_file, 'wb') as f:
                print("writing page")
                f.write(statement_page)
                f.close()
            time.sleep(3)
            driver.back()

            if i >= 9:
                if driver.find_element(By.CLASS_NAME, 'secondary_button').is_enabled():
                    moreBtn = driver.find_element(By.CLASS_NAME, 'secondary_button')
                    moreBtn.click()
                    time.sleep(1)
            time.sleep(5)
            deliveries_table = driver.find_element(By.CLASS_NAME, 'milestone-list-container')
            ventures = deliveries_table.find_elements(By.CLASS_NAME, 'venture-name')
            logging.info(' downloaded pdfs successfully for %s :) '.center(80, "#") % venture_name)

    except Exception as x:
        logging.info(' error during pdf downloading :( '.center(80, "-"))
        logging.info(' Error: %s :( '.center(80, "-") % x)

# Función para descargar un PDF embebido
def download_pdf(link, venture_name):
    try:
        logging.info(' Starting Milestone deliveries download '.center(80, "#"))
        print("Obteniendo contenido")

        cert = requests.certs.where()
        page = requests.get(link, verify=cert, headers={
            "User-Agent": "Mozilla/5.0 (X11; CrOS x86_64 12871.102.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.141 Safari/537.36"})

        print(page)

        if ".pdf" in link:
            print("El contenido es un archivo PDF. Descargando...")
            return page.content  # Devuelve el contenido binario del PDF

        logging.info(' milestone deliveries downloaded successfully for %s :) '.center(80, "#") % venture_name)
        return page.content  # Devuelve el contenido binario de la página

    except Exception as x:
        logging.info(' error during milestone deliveries download %s :( '.center(80, "-") % x)
        print(x)
        return b''


# ################################# Inicio del programa #################################

# Crea una instancia del navegador (en este ejemplo, se utiliza Chrome)
driver = webdriver.Chrome()
driver.maximize_window() # For maximizing window
driver.implicitly_wait(20) # gives an implicit wait for 20 seconds

try:
    # Abre la página de inicio
    driver.get("https://web.nen.wfglobal.org")

    # Espera un tiempo para asegurarte de que la página se cargue completamente
    time.sleep(3)

    # Hacemos login en la página con las credenciales deseadas
    login_NEN('alberto.jimenez@wfglobal.org','Alberto09')

    # Llamamos a la función para obtener la información de todos nuestros cohorts, esto nos da una lista de todos los cohorts, nos permite guardar la lista en un excel y regresa el número de índice del cohort
    selected_cohort=scrap_cohorts()

    # Buscamos en qué página está el cohort y qué número de cohort en la página es, para llevar la página hasta ahí
    locate_cohort(selected_cohort)


    #Call the fuction to open the Milestone deliveries table
    milestone = int(input("Ingresa el número de Milestone que quieres descargar: ")) 
    openMilestone(milestone)
    time.sleep(3)

    download_ventures(driver, dir_path, milestone)
    logging.info(' All actions deployed succesfully '.center(80,"#"))

except Exception as x:
    logging.info(' error during the main execution :( Error: %s'.center(80,"-")%x)
    print("Ha habido un error durante la ejecución")

finally:
    logging.info(' End of program '.center(80,"#"))
    #Esperamos 10 segundos antes de cerrar el navegador
    time.sleep(10)
    # Cierra el navegador
    driver.quit()