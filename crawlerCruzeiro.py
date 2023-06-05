from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(
            'D:/Download/driver/chromedriver.exe')

driver.get('https://estrelabet.com/ptb/bet/main')

driver.maximize_window()

driver.get('https://estrelabet.com/ptb/bet/search/Cruzeiro')

time.sleep(15)

cruzeiro = driver.find_element(By.CSS_SELECTOR,'#container-main > app-fixture-search > div.srch.page > div.modul-accordion.sportType > div.modul-content > div:nth-child(1) > div.modul-content').text.split('\n')

data = cruzeiro[4]
horario = cruzeiro[5]

adiversario = cruzeiro[6]
principal = cruzeiro[7]

vitoriaBh = ' - '.join(cruzeiro[10:12])

empate = ' - '.join(cruzeiro[12:14])
vitoria_cruz=' - '.join(cruzeiro[14:16])
with open ('CruzeiroValor.csv','w') as dados:
        
    print(f"{data} - {horario}|{adiversario} X {principal}|Vitoria - {vitoriaBh} |{empate}|Vitoria - {vitoria_cruz}\n")
    dados.write(f"{data} - {horario}|{adiversario} X {principal}|Vitoria - {vitoriaBh} |{empate}|Vitoria - {vitoria_cruz}\n")

time.sleep(2)
driver.close()