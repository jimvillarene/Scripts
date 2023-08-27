#! /usr/bin/env python3
# Import libraries
import requests, logging
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time, os, re
import pandas as pd

#Inicialización del Logging
filepath='/Users/albertorenejimenezvilla/Documents/Scripts/Curso/Debugging'
debugFile=os.path.join(filepath,'scrapBPI_logging.txt')
logging.basicConfig(filename=debugFile ,level=logging.DEBUG, format='%(asctime)s-%(levelname)s-%(message)s') #filename gets all the errors into a textfile
#logging.disable(logging.DEBUG) #This one disables all logging, so commenting it out cleans all logging messages from critical to lower, othe levels are DEBUG, INFO, WARNING, ERROR, CRITICAL
logging.info(' Start of program '.center(80,"#"))

# Define la función para el proceso de inicio de sesión en PBI
def login_pbi():
    logging.info(' Starting Login '.center(80,"*"))
    try:
        # Abre la página de inicio
        driver.get("https://app.powerbi.com/singleSignOn?pbi_source=websignin_uNav&clientSideAuth=0&ru=https:%2f%2fapp.powerbi.com%2f%3fpbi_source%3dwebsignin_uNav%26clientSideAuth%3d0%26noSignUpCheck%3d1")

        # Espera un tiempo para asegurarte de que la página se cargue completamente
        time.sleep(3)

        # Buscar el elemento de entrada de texto para el correo electrónico y hacer clic en él
        inputBox = driver.find_element(By.CLASS_NAME, "pbi-text-input")
        inputBox.click()

        # Ingresar la dirección de correo electrónico en el campo
        inputBox.send_keys("qliksense.mexico@wfglobal.org")

        # Buscar el botón de envío y hacer clic en él
        submitBtn = driver.find_element(By.CLASS_NAME, "pbi-fluent-button")
        submitBtn.click()

        # Esperar un momento para asegurarse de que la página se cargue después de enviar el correo electrónico
        time.sleep(4)

        # Buscar el campo de contraseña y hacer clic en él
        boxPswrd = driver.find_element(By.CLASS_NAME, 'input')
        boxPswrd.click()

        # Ingresar la contraseña en el campo
        boxPswrd.send_keys("mlogin1-2")

        # Esperar un momento para asegurarse de que la contraseña se ingrese antes de enviar
        time.sleep(1)

        # Buscar el botón de envío (supongo que este es el botón para enviar la contraseña) y hacer clic en él
        submitBtn = driver.find_element(By.CLASS_NAME, "win-button")
        submitBtn.click()

        # Esperar un momento para asegurarse de que la página se cargue después de enviar la contraseña
        time.sleep(3)

        # Buscar un botón (ID:idBtn_Back) y hacer clic en él (supongo que este botón es para retroceder o cancelar alguna acción)
        submitBtn = driver.find_element(By.ID, "idBtn_Back")
        submitBtn.click()

        # Esperar un momento para asegurarse de que la acción de retroceso se complete
        time.sleep(3)
        logging.info(' Log in successfull '.center(80,"#"))

    except Exception as e:
        logging.info(' Error: %s '.center(80,"#")%e)        
        logging.info(' Error during login '.center(80,"#"))
        print("Error:", e)


#Función para incializar el webscrapping de Power BI, accede a la página de WE, después reinicia todos los filtros y selecciona los filtros deseados
def init_NEN():
    try:
        logging.info(' Starting report initialization. Filtering reports '.center(80,"#"))
        #Buscamos y seleccionamos el reporte de WE
        pages = driver.find_elements(By.CLASS_NAME,"name")
        #logging.info((' Value of the reports %s ' % pages.text))
        #print(pages[0].text)
        pages[0].click()
        
        time.sleep(15)


        #Buscamos y seleccionamos el NEN NextGen PV
        nav_tabs = driver.find_elements(By.CLASS_NAME,"mat-list-item-content")
        #logging.info((' Value of the tabs %s ' % pages.text))
        nav_tabs[2].click()
        time.sleep(5)

        # Revisamos si el botón de reset all filters está activo, si es así lo activamos, si no nos brincamos esta instrucción
        if driver.find_element(By.CLASS_NAME,"resetBtn").is_enabled():
            resetBtn=driver.find_element(By.CLASS_NAME,"resetBtn")
            resetBtn.click()
            okBtn=driver.find_element(By.ID,'okButton')
            okBtn.click()
            time.sleep(2)
        
        # Identidicamos el botón de dropdown del RM
        chevron=driver.find_elements(By.CLASS_NAME,"dropdown-chevron")
        chevron[12].click()
        time.sleep(2)
    except Exception as e:
        logging.info(' Error: %s '.center(80,"#")%e)        
        logging.info(' Error during filtering reports  '.center(80,"#"))
        print("Error:", e)

# ################################# Inicio del programa #################################

#Llamamos al función de login e inicialización del driver
# Ruta al controlador del navegador (chromedriver o geckodriver)
# driver_path = 'ruta/al/controlador'

try:
    
    logging.info(' Initializing Webdriver '.center(80,"#"))
    # Crea una instancia del navegador (en este ejemplo, se utiliza Chrome)
    driver = webdriver.Chrome()
    driver.maximize_window()  # Maximiza la ventana del navegador
    driver.implicitly_wait(20)  # Espera implícita de 20 segundos
    logging.info(' Driver initialization successfull '.center(80,"#"))
    login_pbi()

    #Esperamos para que cargue la página, es muy lenta
    time.sleep(20)

    init_NEN()

    # Identidicamos el botón de search de RM y le enviamos el nombre del RM
    comboBoxes=driver.find_elements(By.CLASS_NAME,"searchInput")
    comboBoxes[12].click()
    comboBoxes[12].send_keys("René Jiménez")
    comboBoxes[12].send_keys(Keys.RETURN)
    time.sleep(1)
    checkbox=driver.find_elements(By.CLASS_NAME,'slicerText')
    checkbox[0].click()


    time.sleep(10)

except Exception as e:
    # Cierra el navegador y el archivo de logging
    print("Error:", e)
    logging.info(' Error: %s '.center(80,"*")%e)
    logging.info(' There was an error in the main program, after log in. End of program '.center(80,"*"))
    driver.quit()
finally:
    logging.info(' End of program '.center(80,"#"))
    driver.quit()