from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

#Caminho para o perfil com login manual já feito
PROFILE_PATH = 'https://www.pesquisaprotesto.com.br/consulta'

def consultarProtesto(cnpj):
    options = Options()
    options.add_argument(f"user-data-dir={PROFILE_PATH}")
    driver = webdriver.Chrome(options=options)

    try:
        driver.get("https://www.pesquisaprotesto.com.br/consulta")

        time.sleep(3)

        botao_consulta = driver.find_element(By.XPATH, "//a[@href='/servico/consulta-documento']")
        botao_consulta.click()
        time.sleep(3)

        input_cnpj = driver.find_element(By.ID, "cpf_cnpj")
        input_cnpj.clear()
        input_cnpj.send_keys(cnpj)

        botao = driver.find_element(By.CLASS_NAME, "btn-consultar")
        botao.click()
        time.sleep(4)

        #Adaptar de acordo com o html

        resultado_element = driver.find_element(By.ID, "resultado-consulta")
        resultado_texto = resultado_element.text.strip()

        return resultado_texto if resultado_texto else "Nenhum resultado encontrado"
    
    except Exception as e :
        return f"Erro na consulta: {str(e)}"
    finally:
        driver.quit()