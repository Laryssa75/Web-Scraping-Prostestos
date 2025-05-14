from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#Caminho para o perfil com login manual já feito
PROFILE_PATH = 'C:\Users\LARYSSA\AppData\Local\Google\Chrome\User Data'

def consultarProtesto(cnpj):
    options = Options()
    options.add_argument(f"user-data-dir={PROFILE_PATH}")
    driver = webdriver.Chrome(options=options)

    try:
        driver.get("https://www.pesquisaprotesto.com.br/consulta")

        # time.sleep(3)
        wait = WebDriverWait(driver, 10)
        #botao_consulta = driver.find_element(By.XPATH, "//a[@href='/servico/consulta-documento']")
        botao_consulta = wait.util(EC.element_to_be_clickable((By.XPATH, "//a[@href='/servico/consulta-documento']")))
        botao_consulta.click()
        #time.sleep(3)

        #input_cnpj = driver.find_element(By.ID, "cpf_cnpj")
        input_cnpj = wait.util(EC.presence_of_element_located((By.ID, "cpf_cnpj")))
        input_cnpj.clear()
        input_cnpj.send_keys(cnpj)

        botao = driver.find_element(By.CLASS_NAME, "btn-consultar")
        botao.click()
        #time.sleep(4)

        #Adaptar de acordo com o html

        resultado_element = driver.find_element(By.ID, "resultado-consulta")
        resultado_texto = resultado_element.text.strip()

        return resultado_texto if resultado_texto else "Nenhum resultado encontrado"
    
    except Exception as e :
        return f"Erro na consulta: {str(e)}"
    finally:
        driver.quit()