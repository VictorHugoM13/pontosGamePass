import time
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def search_in_edge(driver, query):
    search_box = driver.find_element(By.NAME, "q")
    search_box.clear()
    search_box.send_keys(query)
    search_box.submit()
    time.sleep(4)

if __name__ == "__main__":
    # Terá que localizar o arquivo msedgedriver.exe e colocar o caminho do mesmo na linha abaixo.
    # Se não tiver o arquivo, faça o download em https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/ e extraia para a pasta do Edge. 
    edge_service = Service('C:\Program Files (x86)\Microsoft\Edge\Application\msedgedriver.exe')
    edge_service.start()
    driver = webdriver.Edge(service=edge_service)
    driver.get("https://www.bing.com/")

    # Aceitando todos os cookies ao abrir o navegador.
    try:
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='bnp_btn_accept']"))).click()
    except:
        pass

    # Fazendo um laço de repetição para pesquisas de 0 a 33. O sistema vai buscar por 0 depois 1 depois 2...    
    for i in range(34):
        query = str(i)
        search_in_edge(driver, query)
        time.sleep(1)
    
       
       