from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import requests
import time
import mysql.connector
import click




#abrindo navegador e página de login do whatsapp
driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com/')
#tempo para fazer login
time.sleep(5)


def bot():
    try:
        #voltando para o contato padrao
        elem = driver.find_element(By.CLASS_NAME, '_1pJ9J _2XH9R')
        elem.click()

        #capturando notificacao
        elem = driver.find_element(By.XPATH, '//*[@id="pane-side"]/div[1]/div/div/div[12]/div/div/div[2]/div[2]/div[2]/span[1]/div/span')
        elem.click()

        #pegando o contato do cliente
        telefone_cliente = driver.find_element(By.CLASS_NAME, '_21nHd')
        #convertendo em texto
        telefone_final = telefone_cliente.text
        print(telefone_final)

        #pegando última mensagem
        todas_as_msg = driver.find_element(By.XPATH, '//*[@id="main"]/div[3]/div/div[2]/div[3]/div[16]/div/div/div/div[1]/div/span[1]/span')
        todas_as_msg_texto = [e.text for e in todas_as_msg]
        msg = todas_as_msg_texto[-1]
        print(msg)


        #respondendo mensagem
        campo_de_texto = driver.find_element(By.XPATH, '_//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]')
        campo_de_texto.click()
        resposta = requests.get("http://localhost:63342/index.php/")





    except:
            print('Buscando mensagens')
            time.sleep(5)
while True:
    bot()